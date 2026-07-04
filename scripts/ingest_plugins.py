#!/usr/bin/env python3
"""
Claude Plugin Catalog Ingestion

Fetches plugins from multiple marketplace sources (official, community,
third-party repos, and GitHub search) and produces a unified plugins.json catalog.

Uses only urllib (no external dependencies). Handles missing/private repos gracefully.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from typing import Any, Optional
import urllib.request
import urllib.error
from urllib.parse import quote, urlencode


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Official and community marketplace repos
MARKETPLACE_REPOS = [
    {
        "owner": "anthropics",
        "repo": "claude-plugins-official",
        "source_type": "official",
        "verified": True,
    },
    {
        "owner": "anthropics",
        "repo": "claude-plugins-community",
        "source_type": "community",
        "verified": False,
    },
]

# Third-party repos known to host Claude plugins
THIRD_PARTY_REPOS = [
    {"owner": "ruvnet", "repo": "ruflo"},
    {"owner": "antonbabenko", "repo": "agent-plugins"},
    {"owner": "AgriciDaniel", "repo": "claude-obsidian"},
    {"owner": "maxbaluev", "repo": "accreted-intelligence"},
    {"owner": "proompteng", "repo": "bilig"},
]

# GitHub search queries to discover additional plugin repos
SEARCH_QUERIES = [
    "path:.claude-plugin filename:plugin.json",
    "claude-code plugin.json in:path",
]

# Capability keywords to scan for in manifests and READMEs
CAPABILITY_KEYWORDS = {
    "skills": ["skill", "slash command", "/"],
    "agents": ["agent", "subagent", "agent_type"],
    "hooks": ["hook", "pre-commit", "post-commit", "pre-tool", "post-tool"],
    "mcp": ["mcp", "model context protocol", "mcp_server", "mcpServers"],
    "monitors": ["monitor", "watch", "observe", "stream"],
}

# Compatibility keywords
COMPAT_KEYWORDS = {
    "claude-code": ["claude-code", "claude code", "anthropic", ".claude"],
    "cursor": ["cursor", "cursorless"],
    "copilot": ["copilot", "github copilot"],
    "gemini-cli": ["gemini-cli", "gemini cli", "google gemini"],
    "codex": ["codex", "openai codex"],
}

# Output path
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "plugins.json")


# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------

def github_headers() -> dict[str, str]:
    """Return headers for GitHub API requests."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "agent-skills-directory/ingest-plugins",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def github_request(url: str) -> Optional[dict[str, Any]]:
    """Make a GET request to the GitHub API. Returns parsed JSON or None on error."""
    req = urllib.request.Request(url, headers=github_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code in (404, 403, 451):
            return None
        print(f"  [WARN] HTTP {e.code} for {url}", file=sys.stderr)
        return None
    except (urllib.error.URLError, OSError) as e:
        print(f"  [WARN] Network error for {url}: {e}", file=sys.stderr)
        return None


def github_raw(owner: str, repo: str, path: str, branch: str = "main") -> Optional[str]:
    """Fetch raw file content from GitHub."""
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "agent-skills-directory/ingest-plugins",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8")
    except (urllib.error.HTTPError, urllib.error.URLError, OSError):
        return None


def get_repo_info(owner: str, repo: str) -> Optional[dict[str, Any]]:
    """Get repository metadata from GitHub API."""
    url = f"https://api.github.com/repos/{owner}/{repo}"
    return github_request(url)


def get_repo_tree(owner: str, repo: str, branch: str = "main") -> Optional[list[dict[str, Any]]]:
    """Get the full file tree of a repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    data = github_request(url)
    if data and "tree" in data:
        return data["tree"]
    return None


def search_repos(query: str) -> list[dict[str, Any]]:
    """Search GitHub for repositories matching a query."""
    encoded = urlencode({"q": query, "per_page": "30"})
    url = f"https://api.github.com/search/repositories?{encoded}"
    data = github_request(url)
    if data and "items" in data:
        return data["items"]
    return []


def search_code(query: str) -> list[dict[str, Any]]:
    """Search GitHub code for files matching a query."""
    encoded = urlencode({"q": query, "per_page": "30"})
    url = f"https://api.github.com/search/code?{encoded}"
    data = github_request(url)
    if data and "items" in data:
        return data["items"]
    return []


# ---------------------------------------------------------------------------
# Plugin extraction
# ---------------------------------------------------------------------------

def extract_capabilities(text: str) -> list[str]:
    """Detect plugin capabilities from text content."""
    text_lower = text.lower()
    capabilities = []
    for cap, keywords in CAPABILITY_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            capabilities.append(cap)
    return capabilities


def extract_compatibility(text: str) -> list[str]:
    """Detect tool compatibility from text content."""
    text_lower = text.lower()
    compat = []
    for tool, keywords in COMPAT_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            compat.append(tool)
    # Default to claude-code if nothing else detected
    if not compat:
        compat = ["claude-code"]
    return compat


def extract_tags(text: str) -> list[str]:
    """Extract relevant tags from description/readme text."""
    tag_patterns = [
        r"(?:automation|devops|ci/cd|testing|deployment)",
        r"(?:ai|ml|llm|nlp|generative)",
        r"(?:security|auth|encryption)",
        r"(?:database|storage|cache)",
        r"(?:api|rest|graphql|grpc)",
        r"(?:monitoring|logging|observability)",
        r"(?:documentation|docs|wiki)",
        r"(?:code.?review|linting|formatting)",
        r"(?:git|version.?control|vcs)",
        r"(?:cloud|aws|gcp|azure)",
        r"(?:container|docker|kubernetes|k8s)",
        r"(?:web|frontend|backend|fullstack)",
        r"(?:productivity|workflow|task)",
        r"(?:research|analysis|data)",
    ]
    text_lower = text.lower()
    tags = []
    for pattern in tag_patterns:
        match = re.search(pattern, text_lower)
        if match:
            # Normalize the tag
            tag = match.group(0).replace(" ", "-")
            # Simplify compound tags
            tag = re.sub(r"[.?]", "", tag)
            tags.append(tag)
    return sorted(set(tags))


def parse_plugin_manifest(manifest_str: str) -> Optional[dict[str, Any]]:
    """Parse a plugin.json manifest file content."""
    try:
        return json.loads(manifest_str)
    except (json.JSONDecodeError, ValueError):
        return None


def build_plugin_entry(
    owner: str,
    repo: str,
    manifest: Optional[dict[str, Any]],
    repo_info: Optional[dict[str, Any]],
    source_type: str,
    verified: bool,
    readme_text: str = "",
) -> dict[str, Any]:
    """Build a normalized plugin entry from available data."""
    plugin_id = f"{owner}/{repo}"

    # Derive name from manifest, repo info, or repo name
    name = ""
    if manifest and manifest.get("name"):
        name = manifest["name"]
    elif repo_info and repo_info.get("name"):
        name = repo_info["name"].replace("-", " ").replace("_", " ").title()
    else:
        name = repo.replace("-", " ").replace("_", " ").title()

    # Derive description
    description = ""
    if manifest and manifest.get("description"):
        description = manifest["description"]
    elif repo_info and repo_info.get("description"):
        description = repo_info["description"]
    else:
        description = f"Claude Code plugin from {owner}/{repo}"

    # Combine text for analysis
    combined_text = " ".join(filter(None, [
        description,
        readme_text,
        json.dumps(manifest) if manifest else "",
    ]))

    # Stars as install proxy
    stars = 0
    if repo_info and repo_info.get("stargazers_count"):
        stars = repo_info["stargazers_count"]

    # Last updated
    last_updated = ""
    if repo_info and repo_info.get("pushed_at"):
        last_updated = repo_info["pushed_at"]
    elif repo_info and repo_info.get("updated_at"):
        last_updated = repo_info["updated_at"]

    # Extract capabilities and compatibility
    capabilities = extract_capabilities(combined_text)
    if manifest:
        # Also check manifest keys for capabilities
        if manifest.get("skills") or manifest.get("commands"):
            if "skills" not in capabilities:
                capabilities.append("skills")
        if manifest.get("agents") or manifest.get("agent_types"):
            if "agents" not in capabilities:
                capabilities.append("agents")
        if manifest.get("hooks"):
            if "hooks" not in capabilities:
                capabilities.append("hooks")
        if manifest.get("mcp") or manifest.get("mcpServers"):
            if "mcp" not in capabilities:
                capabilities.append("mcp")

    compatibility = extract_compatibility(combined_text)
    tags = extract_tags(combined_text)

    return {
        "id": plugin_id,
        "name": name,
        "description": description,
        "source_repo": f"https://github.com/{owner}/{repo}",
        "source_type": source_type,
        "install_count": stars,
        "verified": verified,
        "capabilities": sorted(capabilities),
        "tags": tags,
        "last_updated": last_updated,
        "compatibility": sorted(compatibility),
    }


# ---------------------------------------------------------------------------
# Source ingestion
# ---------------------------------------------------------------------------

def ingest_marketplace_repo(config: dict[str, Any]) -> list[dict[str, Any]]:
    """Ingest plugins from an official/community marketplace repo."""
    owner = config["owner"]
    repo = config["repo"]
    source_type = config["source_type"]
    verified = config["verified"]
    plugins = []

    print(f"  Scanning {owner}/{repo} ({source_type})...")

    # First try to fetch a marketplace.json index
    marketplace_json = github_raw(owner, repo, "marketplace.json")
    if marketplace_json:
        try:
            index = json.loads(marketplace_json)
            entries = index if isinstance(index, list) else index.get("plugins", [])
            repo_info = get_repo_info(owner, repo)
            for entry in entries:
                plugin_owner = entry.get("owner", owner)
                plugin_repo = entry.get("repo", entry.get("name", repo))
                plugin = build_plugin_entry(
                    owner=plugin_owner,
                    repo=plugin_repo,
                    manifest=entry,
                    repo_info=repo_info,
                    source_type=source_type,
                    verified=verified,
                )
                plugins.append(plugin)
            print(f"    Found {len(plugins)} plugins via marketplace.json")
            return plugins
        except (json.JSONDecodeError, ValueError):
            pass

    # Fallback: scan repo tree for .claude-plugin/plugin.json files
    tree = get_repo_tree(owner, repo)
    if not tree:
        print(f"    Repository not accessible, skipping.")
        return plugins

    repo_info = get_repo_info(owner, repo)
    manifest_paths = [
        item["path"] for item in tree
        if item.get("type") == "blob" and item["path"].endswith("plugin.json")
        and ".claude-plugin" in item["path"]
    ]

    for path in manifest_paths:
        content = github_raw(owner, repo, path)
        if not content:
            continue
        manifest = parse_plugin_manifest(content)
        if not manifest:
            continue

        # Determine plugin identity from path
        # e.g. plugins/my-plugin/.claude-plugin/plugin.json -> my-plugin
        parts = path.split("/")
        plugin_name = parts[-3] if len(parts) >= 3 else parts[0]

        plugin = build_plugin_entry(
            owner=owner,
            repo=plugin_name,
            manifest=manifest,
            repo_info=repo_info,
            source_type=source_type,
            verified=verified,
        )
        plugins.append(plugin)
        # Respect rate limits
        time.sleep(0.5)

    print(f"    Found {len(plugins)} plugins via tree scan")
    return plugins


def ingest_third_party_repo(config: dict[str, str]) -> Optional[dict[str, Any]]:
    """Ingest a single third-party repo as a plugin."""
    owner = config["owner"]
    repo = config["repo"]

    print(f"  Scanning {owner}/{repo} (third-party)...")

    repo_info = get_repo_info(owner, repo)
    if not repo_info:
        print(f"    Repository not accessible, skipping.")
        return None

    # Try to find plugin manifest
    manifest = None
    manifest_content = github_raw(owner, repo, ".claude-plugin/plugin.json")
    if manifest_content:
        manifest = parse_plugin_manifest(manifest_content)
    else:
        # Try alternate locations
        for alt_path in ["plugin.json", "claude-plugin.json", ".claude/plugin.json"]:
            content = github_raw(owner, repo, alt_path)
            if content:
                manifest = parse_plugin_manifest(content)
                if manifest:
                    break

    # Fetch README for analysis
    readme_text = ""
    for readme_name in ["README.md", "readme.md", "README.rst", "README"]:
        content = github_raw(owner, repo, readme_name)
        if content:
            readme_text = content[:5000]  # Cap to avoid huge READMEs
            break

    plugin = build_plugin_entry(
        owner=owner,
        repo=repo,
        manifest=manifest,
        repo_info=repo_info,
        source_type="third-party",
        verified=False,
        readme_text=readme_text,
    )
    return plugin


def ingest_github_search() -> list[dict[str, Any]]:
    """Discover plugins via GitHub search."""
    plugins = []
    seen_repos: set[str] = set()

    for query in SEARCH_QUERIES:
        print(f"  Searching: '{query}'...")

        # Search code for plugin.json files
        results = search_code(query)
        for item in results:
            repo_data = item.get("repository", {})
            full_name = repo_data.get("full_name", "")
            if not full_name or full_name in seen_repos:
                continue
            seen_repos.add(full_name)

            owner, repo = full_name.split("/", 1)
            repo_info = get_repo_info(owner, repo)
            if not repo_info:
                continue

            # Try to get the plugin manifest
            manifest = None
            file_path = item.get("path", "")
            if file_path.endswith("plugin.json"):
                content = github_raw(owner, repo, file_path)
                if content:
                    manifest = parse_plugin_manifest(content)

            # Fetch README
            readme_text = ""
            readme_content = github_raw(owner, repo, "README.md")
            if readme_content:
                readme_text = readme_content[:5000]

            plugin = build_plugin_entry(
                owner=owner,
                repo=repo,
                manifest=manifest,
                repo_info=repo_info,
                source_type="discovered",
                verified=False,
                readme_text=readme_text,
            )
            plugins.append(plugin)

            # Respect rate limits
            time.sleep(1.0)

        # Also search for repos by topic
        repo_results = search_repos(query)
        for repo_data in repo_results:
            full_name = repo_data.get("full_name", "")
            if not full_name or full_name in seen_repos:
                continue
            seen_repos.add(full_name)

            owner, repo = full_name.split("/", 1)

            plugin = build_plugin_entry(
                owner=owner,
                repo=repo,
                manifest=None,
                repo_info=repo_data,
                source_type="discovered",
                verified=False,
            )
            plugins.append(plugin)
            time.sleep(0.5)

    print(f"    Discovered {len(plugins)} plugins via search")
    return plugins


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def deduplicate_plugins(plugins: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Deduplicate plugins by ID, preferring higher-priority source types."""
    priority = {"official": 0, "community": 1, "third-party": 2, "discovered": 3}
    seen: dict[str, dict[str, Any]] = {}

    for plugin in plugins:
        pid = plugin["id"]
        if pid not in seen:
            seen[pid] = plugin
        else:
            existing_priority = priority.get(seen[pid]["source_type"], 99)
            new_priority = priority.get(plugin["source_type"], 99)
            if new_priority < existing_priority:
                seen[pid] = plugin

    return sorted(seen.values(), key=lambda p: (priority.get(p["source_type"], 99), p["id"]))


def main() -> None:
    """Main entry point for plugin ingestion."""
    print("=" * 60)
    print("Claude Plugin Catalog Ingestion")
    print("=" * 60)
    print()

    if not GITHUB_TOKEN:
        print("[INFO] No GITHUB_TOKEN set. Rate limits will be restrictive.")
        print("       Set GITHUB_TOKEN env var for better results.")
        print()

    all_plugins: list[dict[str, Any]] = []
    sources_scanned: list[str] = []
    errors: list[str] = []

    # 1. Ingest official/community marketplace repos
    print("[1/4] Scanning marketplace repos...")
    for config in MARKETPLACE_REPOS:
        source_id = f"{config['owner']}/{config['repo']}"
        sources_scanned.append(source_id)
        try:
            plugins = ingest_marketplace_repo(config)
            all_plugins.extend(plugins)
        except Exception as e:
            errors.append(f"{source_id}: {e}")
            print(f"    [ERROR] {e}", file=sys.stderr)
    print()

    # 2. Ingest third-party repos
    print("[2/4] Scanning third-party repos...")
    for config in THIRD_PARTY_REPOS:
        source_id = f"{config['owner']}/{config['repo']}"
        sources_scanned.append(source_id)
        try:
            plugin = ingest_third_party_repo(config)
            if plugin:
                all_plugins.append(plugin)
        except Exception as e:
            errors.append(f"{source_id}: {e}")
            print(f"    [ERROR] {e}", file=sys.stderr)
        time.sleep(0.5)
    print()

    # 3. GitHub search discovery
    print("[3/4] Searching GitHub for plugin repos...")
    try:
        discovered = ingest_github_search()
        all_plugins.extend(discovered)
        sources_scanned.append("github-search")
    except Exception as e:
        errors.append(f"github-search: {e}")
        print(f"  [ERROR] {e}", file=sys.stderr)
    print()

    # 4. Deduplicate and finalize
    print("[4/4] Deduplicating and building catalog...")
    final_plugins = deduplicate_plugins(all_plugins)
    print(f"  {len(all_plugins)} raw -> {len(final_plugins)} deduplicated plugins")
    print()

    # Build output
    catalog = {
        "metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_plugins": len(final_plugins),
            "sources_scanned": sources_scanned,
            "errors": errors if errors else None,
        },
        "plugins": final_plugins,
    }

    # Write output
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    print("=" * 60)
    print(f"Catalog written to: {OUTPUT_PATH}")
    print(f"Total plugins: {len(final_plugins)}")
    print(f"Sources scanned: {len(sources_scanned)}")
    if errors:
        print(f"Errors: {len(errors)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
