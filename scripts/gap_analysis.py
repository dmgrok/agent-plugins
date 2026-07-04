#!/usr/bin/env python3
"""
Gap Analysis Script for Agent Skills Directory

Reads plugins.json (the plugin catalog) and taxonomy.json (capability taxonomy + personas),
maps plugin capabilities to taxonomy categories via keyword matching, computes coverage
per persona, and outputs gap_analysis.json with actionable recommendations.

Usage:
    python3 scripts/gap_analysis.py
"""

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

PLUGINS_PATH = PROJECT_ROOT / "plugins.json"
TAXONOMY_PATH = PROJECT_ROOT / "taxonomy.json"
OUTPUT_PATH = PROJECT_ROOT / "gap_analysis.json"

# Fallback: if plugins.json not found, try catalog.json (same structure)
CATALOG_FALLBACK_PATH = PROJECT_ROOT / "catalog.json"


# ---------------------------------------------------------------------------
# Default Taxonomy (used when taxonomy.json does not exist)
# ---------------------------------------------------------------------------

DEFAULT_TAXONOMY = {
    "version": "1.0.0",
    "categories": {
        "code-generation": {
            "description": "Automated code creation, scaffolding, and boilerplate generation",
            "subcategories": {
                "scaffolding": "Project and component scaffolding",
                "refactoring": "Automated code refactoring and modernization",
                "code-review": "Automated code review and linting",
                "pair-programming": "Interactive coding assistance"
            }
        },
        "testing": {
            "description": "Test creation, execution, and coverage analysis",
            "subcategories": {
                "unit-tests": "Unit test generation and execution",
                "integration-tests": "Integration and end-to-end testing",
                "performance-tests": "Load testing and benchmarking",
                "test-coverage": "Coverage analysis and reporting"
            }
        },
        "documentation-knowledge": {
            "description": "Documentation generation, knowledge management, and search",
            "subcategories": {
                "api-docs": "API documentation generation",
                "technical-writing": "Technical documentation and guides",
                "knowledge-base": "Knowledge management and retrieval",
                "changelog": "Changelog and release notes generation"
            }
        },
        "devops-deployment": {
            "description": "CI/CD, containerization, infrastructure as code",
            "subcategories": {
                "ci-pipelines": "Continuous integration setup and management",
                "cd-pipelines": "Continuous deployment and release automation",
                "containerization": "Docker, Kubernetes, container orchestration",
                "infrastructure-as-code": "Terraform, CDK, CloudFormation"
            }
        },
        "design-frontend": {
            "description": "UI/UX design, component libraries, styling",
            "subcategories": {
                "component-libraries": "React, Vue, Angular component development",
                "styling": "CSS, Tailwind, design systems",
                "accessibility": "WCAG compliance and a11y testing",
                "responsive-design": "Mobile-first and responsive layouts"
            }
        },
        "data-analytics": {
            "description": "Data processing, analysis, visualization, and pipelines",
            "subcategories": {
                "data-pipelines": "ETL, data ingestion, streaming",
                "visualization": "Charts, dashboards, reporting",
                "database": "Database design, queries, optimization",
                "data-science": "Statistical analysis and ML data prep"
            }
        },
        "security": {
            "description": "Security scanning, compliance, and vulnerability management",
            "subcategories": {
                "vulnerability-scanning": "SAST, DAST, dependency scanning",
                "compliance": "SOC2, HIPAA, GDPR compliance checks",
                "auth-identity": "Authentication and authorization patterns",
                "secrets-management": "Secret rotation, vault management"
            }
        },
        "cloud-infrastructure": {
            "description": "Cloud provider services, serverless, and scaling",
            "subcategories": {
                "aws": "Amazon Web Services specific tooling",
                "azure": "Microsoft Azure specific tooling",
                "gcp": "Google Cloud Platform specific tooling",
                "serverless": "Lambda, Functions, serverless architectures"
            }
        },
        "ml-ai": {
            "description": "Machine learning, AI model training, and inference",
            "subcategories": {
                "model-training": "Model training and fine-tuning",
                "inference": "Model serving and inference optimization",
                "prompt-engineering": "Prompt design and optimization",
                "mlops": "ML pipeline management and monitoring"
            }
        },
        "mobile-development": {
            "description": "Native and cross-platform mobile app development",
            "subcategories": {
                "ios": "iOS and Swift development",
                "android": "Android and Kotlin development",
                "cross-platform": "React Native, Flutter, Expo",
                "app-store": "App store submission and management"
            }
        },
        "project-management": {
            "description": "Task tracking, sprint planning, and workflow automation",
            "subcategories": {
                "task-tracking": "Issue tracking and backlog management",
                "sprint-planning": "Agile ceremonies and sprint management",
                "workflow-automation": "Process automation and integrations",
                "reporting": "Status reports and metrics dashboards"
            }
        },
        "communication": {
            "description": "Team communication, content creation, and collaboration",
            "subcategories": {
                "email": "Email drafting and automation",
                "content-creation": "Blog posts, marketing copy, social media",
                "collaboration": "Team messaging and knowledge sharing",
                "presentations": "Slide decks and visual communications"
            }
        },
        "api-integrations": {
            "description": "Third-party API connections and webhook management",
            "subcategories": {
                "rest-apis": "REST API design and consumption",
                "graphql": "GraphQL schema and resolver development",
                "webhooks": "Event-driven integration patterns",
                "sdk-generation": "Client SDK and wrapper generation"
            }
        },
        "version-control": {
            "description": "Git workflows, branching strategies, and code collaboration",
            "subcategories": {
                "git-workflows": "Branching, merging, and PR management",
                "monorepo": "Monorepo tooling and management",
                "code-collaboration": "Code review workflows and pair programming",
                "release-management": "Versioning, tagging, and release automation"
            }
        }
    },
    "personas": {
        "knowledge-worker": {
            "name": "Knowledge Worker",
            "description": "Non-technical professional who needs AI assistance for documentation, communication, and analysis",
            "relevant_categories": [
                "documentation-knowledge",
                "communication",
                "data-analytics",
                "project-management"
            ]
        },
        "frontend-developer": {
            "name": "Frontend Developer",
            "description": "Developer focused on user interfaces, design systems, and client-side applications",
            "relevant_categories": [
                "design-frontend",
                "code-generation",
                "testing",
                "mobile-development",
                "api-integrations"
            ]
        },
        "backend-developer": {
            "name": "Backend Developer",
            "description": "Developer focused on APIs, databases, and server-side logic",
            "relevant_categories": [
                "code-generation",
                "testing",
                "data-analytics",
                "api-integrations",
                "devops-deployment",
                "security"
            ]
        },
        "devops-engineer": {
            "name": "DevOps Engineer",
            "description": "Engineer focused on deployment pipelines, infrastructure, and operational reliability",
            "relevant_categories": [
                "devops-deployment",
                "cloud-infrastructure",
                "security",
                "version-control",
                "testing"
            ]
        },
        "data-scientist": {
            "name": "Data Scientist",
            "description": "Professional working with data analysis, ML models, and statistical methods",
            "relevant_categories": [
                "ml-ai",
                "data-analytics",
                "code-generation",
                "documentation-knowledge"
            ]
        },
        "fullstack-developer": {
            "name": "Full-Stack Developer",
            "description": "Developer working across the entire application stack",
            "relevant_categories": [
                "code-generation",
                "design-frontend",
                "testing",
                "devops-deployment",
                "api-integrations",
                "data-analytics",
                "version-control"
            ]
        },
        "mobile-developer": {
            "name": "Mobile Developer",
            "description": "Developer building native or cross-platform mobile applications",
            "relevant_categories": [
                "mobile-development",
                "design-frontend",
                "testing",
                "code-generation",
                "devops-deployment"
            ]
        },
        "security-engineer": {
            "name": "Security Engineer",
            "description": "Engineer focused on application and infrastructure security",
            "relevant_categories": [
                "security",
                "cloud-infrastructure",
                "devops-deployment",
                "testing",
                "code-generation"
            ]
        },
        "engineering-manager": {
            "name": "Engineering Manager",
            "description": "Technical leader managing teams, projects, and delivery",
            "relevant_categories": [
                "project-management",
                "documentation-knowledge",
                "communication",
                "version-control",
                "testing"
            ]
        }
    }
}


# ---------------------------------------------------------------------------
# Keyword -> Category Mapping Heuristics
# ---------------------------------------------------------------------------

# Maps keywords found in plugin name/description/tags to taxonomy categories
# Format: keyword -> "category/subcategory" or just "category"
KEYWORD_CATEGORY_MAP = {
    # code-generation
    "scaffold": "code-generation/scaffolding",
    "scaffolding": "code-generation/scaffolding",
    "boilerplate": "code-generation/scaffolding",
    "generator": "code-generation/scaffolding",
    "template": "code-generation/scaffolding",
    "starter": "code-generation/scaffolding",
    "bootstrap": "code-generation/scaffolding",
    "refactor": "code-generation/refactoring",
    "refactoring": "code-generation/refactoring",
    "modernize": "code-generation/refactoring",
    "migration": "code-generation/refactoring",
    "upgrade": "code-generation/refactoring",
    "code-review": "code-generation/code-review",
    "lint": "code-generation/code-review",
    "linting": "code-generation/code-review",
    "eslint": "code-generation/code-review",
    "prettier": "code-generation/code-review",
    "format": "code-generation/code-review",
    "pair": "code-generation/pair-programming",
    "copilot": "code-generation/pair-programming",
    "autocomplete": "code-generation/pair-programming",
    "completion": "code-generation/pair-programming",
    "coder": "code-generation/pair-programming",
    "coding": "code-generation/pair-programming",
    "code": "code-generation",

    # testing
    "test": "testing/unit-tests",
    "testing": "testing/unit-tests",
    "unittest": "testing/unit-tests",
    "jest": "testing/unit-tests",
    "pytest": "testing/unit-tests",
    "mocha": "testing/unit-tests",
    "vitest": "testing/unit-tests",
    "integration-test": "testing/integration-tests",
    "e2e": "testing/integration-tests",
    "end-to-end": "testing/integration-tests",
    "cypress": "testing/integration-tests",
    "playwright": "testing/integration-tests",
    "selenium": "testing/integration-tests",
    "performance": "testing/performance-tests",
    "benchmark": "testing/performance-tests",
    "load-test": "testing/performance-tests",
    "coverage": "testing/test-coverage",
    "qa": "testing",

    # documentation-knowledge
    "docs": "documentation-knowledge/api-docs",
    "documentation": "documentation-knowledge/technical-writing",
    "readme": "documentation-knowledge/technical-writing",
    "wiki": "documentation-knowledge/knowledge-base",
    "knowledge": "documentation-knowledge/knowledge-base",
    "search": "documentation-knowledge/knowledge-base",
    "changelog": "documentation-knowledge/changelog",
    "release-notes": "documentation-knowledge/changelog",
    "technical-writing": "documentation-knowledge/technical-writing",
    "guide": "documentation-knowledge/technical-writing",
    "tutorial": "documentation-knowledge/technical-writing",

    # devops-deployment
    "ci": "devops-deployment/ci-pipelines",
    "cicd": "devops-deployment/ci-pipelines",
    "github-actions": "devops-deployment/ci-pipelines",
    "jenkins": "devops-deployment/ci-pipelines",
    "pipeline": "devops-deployment/ci-pipelines",
    "deploy": "devops-deployment/cd-pipelines",
    "deployment": "devops-deployment/cd-pipelines",
    "release": "devops-deployment/cd-pipelines",
    "vercel": "devops-deployment/cd-pipelines",
    "netlify": "devops-deployment/cd-pipelines",
    "docker": "devops-deployment/containerization",
    "container": "devops-deployment/containerization",
    "kubernetes": "devops-deployment/containerization",
    "k8s": "devops-deployment/containerization",
    "helm": "devops-deployment/containerization",
    "terraform": "devops-deployment/infrastructure-as-code",
    "cdk": "devops-deployment/infrastructure-as-code",
    "cloudformation": "devops-deployment/infrastructure-as-code",
    "pulumi": "devops-deployment/infrastructure-as-code",
    "iac": "devops-deployment/infrastructure-as-code",
    "infra": "devops-deployment/infrastructure-as-code",
    "devops": "devops-deployment",

    # design-frontend
    "react": "design-frontend/component-libraries",
    "vue": "design-frontend/component-libraries",
    "angular": "design-frontend/component-libraries",
    "svelte": "design-frontend/component-libraries",
    "component": "design-frontend/component-libraries",
    "ui": "design-frontend/component-libraries",
    "frontend": "design-frontend/component-libraries",
    "tailwind": "design-frontend/styling",
    "css": "design-frontend/styling",
    "sass": "design-frontend/styling",
    "design-system": "design-frontend/styling",
    "styling": "design-frontend/styling",
    "theme": "design-frontend/styling",
    "a11y": "design-frontend/accessibility",
    "accessibility": "design-frontend/accessibility",
    "wcag": "design-frontend/accessibility",
    "responsive": "design-frontend/responsive-design",
    "mobile-first": "design-frontend/responsive-design",
    "design": "design-frontend",
    "web": "design-frontend",

    # data-analytics
    "etl": "data-analytics/data-pipelines",
    "pipeline": "data-analytics/data-pipelines",
    "streaming": "data-analytics/data-pipelines",
    "kafka": "data-analytics/data-pipelines",
    "chart": "data-analytics/visualization",
    "dashboard": "data-analytics/visualization",
    "visualization": "data-analytics/visualization",
    "grafana": "data-analytics/visualization",
    "database": "data-analytics/database",
    "sql": "data-analytics/database",
    "postgres": "data-analytics/database",
    "mysql": "data-analytics/database",
    "mongodb": "data-analytics/database",
    "redis": "data-analytics/database",
    "supabase": "data-analytics/database",
    "prisma": "data-analytics/database",
    "analytics": "data-analytics/data-science",
    "statistics": "data-analytics/data-science",
    "pandas": "data-analytics/data-science",
    "numpy": "data-analytics/data-science",
    "data": "data-analytics",
    "bigquery": "data-analytics/database",

    # security
    "vulnerability": "security/vulnerability-scanning",
    "sast": "security/vulnerability-scanning",
    "dast": "security/vulnerability-scanning",
    "scan": "security/vulnerability-scanning",
    "security": "security/vulnerability-scanning",
    "pentest": "security/vulnerability-scanning",
    "compliance": "security/compliance",
    "soc2": "security/compliance",
    "hipaa": "security/compliance",
    "gdpr": "security/compliance",
    "audit": "security/compliance",
    "auth": "security/auth-identity",
    "authentication": "security/auth-identity",
    "oauth": "security/auth-identity",
    "identity": "security/auth-identity",
    "secrets": "security/secrets-management",
    "vault": "security/secrets-management",
    "encryption": "security/secrets-management",

    # cloud-infrastructure
    "aws": "cloud-infrastructure/aws",
    "amazon": "cloud-infrastructure/aws",
    "lambda": "cloud-infrastructure/serverless",
    "s3": "cloud-infrastructure/aws",
    "ec2": "cloud-infrastructure/aws",
    "azure": "cloud-infrastructure/azure",
    "gcp": "cloud-infrastructure/gcp",
    "google-cloud": "cloud-infrastructure/gcp",
    "firebase": "cloud-infrastructure/gcp",
    "serverless": "cloud-infrastructure/serverless",
    "cloud": "cloud-infrastructure",
    "cloudflare": "cloud-infrastructure",
    "cloudwatch": "cloud-infrastructure/aws",

    # ml-ai
    "ml": "ml-ai/model-training",
    "machine-learning": "ml-ai/model-training",
    "training": "ml-ai/model-training",
    "fine-tune": "ml-ai/model-training",
    "huggingface": "ml-ai/model-training",
    "pytorch": "ml-ai/model-training",
    "tensorflow": "ml-ai/model-training",
    "inference": "ml-ai/inference",
    "model": "ml-ai/inference",
    "serving": "ml-ai/inference",
    "prompt": "ml-ai/prompt-engineering",
    "prompt-engineering": "ml-ai/prompt-engineering",
    "llm": "ml-ai/prompt-engineering",
    "gpt": "ml-ai/prompt-engineering",
    "ai": "ml-ai",
    "agent": "ml-ai",
    "mlops": "ml-ai/mlops",
    "experiment": "ml-ai/mlops",

    # mobile-development
    "ios": "mobile-development/ios",
    "swift": "mobile-development/ios",
    "xcode": "mobile-development/ios",
    "swiftui": "mobile-development/ios",
    "android": "mobile-development/android",
    "kotlin": "mobile-development/android",
    "react-native": "mobile-development/cross-platform",
    "expo": "mobile-development/cross-platform",
    "flutter": "mobile-development/cross-platform",
    "mobile": "mobile-development/cross-platform",
    "app-store": "mobile-development/app-store",
    "appstore": "mobile-development/app-store",

    # project-management
    "jira": "project-management/task-tracking",
    "issue": "project-management/task-tracking",
    "backlog": "project-management/task-tracking",
    "task": "project-management/task-tracking",
    "sprint": "project-management/sprint-planning",
    "agile": "project-management/sprint-planning",
    "scrum": "project-management/sprint-planning",
    "kanban": "project-management/sprint-planning",
    "workflow": "project-management/workflow-automation",
    "automation": "project-management/workflow-automation",
    "project": "project-management",
    "planning": "project-management/sprint-planning",

    # communication
    "email": "communication/email",
    "slack": "communication/collaboration",
    "teams": "communication/collaboration",
    "discord": "communication/collaboration",
    "blog": "communication/content-creation",
    "content": "communication/content-creation",
    "copywriting": "communication/content-creation",
    "marketing": "communication/content-creation",
    "seo": "communication/content-creation",
    "social": "communication/content-creation",
    "presentation": "communication/presentations",
    "slides": "communication/presentations",
    "communication": "communication",
    "writing": "communication/content-creation",

    # api-integrations
    "api": "api-integrations/rest-apis",
    "rest": "api-integrations/rest-apis",
    "graphql": "api-integrations/graphql",
    "webhook": "api-integrations/webhooks",
    "sdk": "api-integrations/sdk-generation",
    "client": "api-integrations/sdk-generation",
    "integration": "api-integrations",
    "connector": "api-integrations",

    # version-control
    "git": "version-control/git-workflows",
    "branch": "version-control/git-workflows",
    "merge": "version-control/git-workflows",
    "pr": "version-control/git-workflows",
    "pull-request": "version-control/git-workflows",
    "monorepo": "version-control/monorepo",
    "turborepo": "version-control/monorepo",
    "nx": "version-control/monorepo",
    "lerna": "version-control/monorepo",
    "version": "version-control/release-management",
    "tag": "version-control/release-management",
    "semver": "version-control/release-management",
}


# ---------------------------------------------------------------------------
# Core Functions
# ---------------------------------------------------------------------------

def load_plugins():
    """Load plugin catalog from plugins.json or catalog.json fallback."""
    if PLUGINS_PATH.exists():
        with open(PLUGINS_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    elif CATALOG_FALLBACK_PATH.exists():
        with open(CATALOG_FALLBACK_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        raise FileNotFoundError(
            f"Neither {PLUGINS_PATH} nor {CATALOG_FALLBACK_PATH} found. "
            "Please ensure the plugin catalog exists."
        )

    # Handle both list-of-plugins and dict-with-skills-key formats
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return data.get("skills", data.get("plugins", []))
    return []


def normalize_taxonomy(raw):
    """Convert list-based taxonomy.json format to dict-based format the script expects."""
    result = {}

    # Handle categories: list of {id, name, description, subcategories: [...]} -> dict
    cats_raw = raw.get("taxonomy", {}).get("categories", raw.get("categories", []))
    if isinstance(cats_raw, list):
        categories = {}
        for cat in cats_raw:
            cat_id = cat.get("id", "")
            subcats = {}
            for sub in cat.get("subcategories", []):
                subcats[sub.get("id", "")] = sub.get("description", sub.get("name", ""))
            categories[cat_id] = {
                "description": cat.get("description", cat.get("name", "")),
                "subcategories": subcats,
            }
        result["categories"] = categories
    elif isinstance(cats_raw, dict):
        result["categories"] = cats_raw
    else:
        result["categories"] = {}

    # Handle personas: list of {id, name, ...} -> dict keyed by id
    personas_raw = raw.get("personas", [])
    if isinstance(personas_raw, list):
        result["personas"] = {p["id"]: p for p in personas_raw if "id" in p}
    elif isinstance(personas_raw, dict):
        result["personas"] = personas_raw
    else:
        result["personas"] = {}

    # Carry over compatibility if present
    if "compatibility" in raw:
        result["compatibility"] = raw["compatibility"]

    result["version"] = raw.get("version", "1.0.0")
    return result


def load_taxonomy():
    """Load taxonomy from taxonomy.json or use default."""
    if TAXONOMY_PATH.exists():
        with open(TAXONOMY_PATH, "r", encoding="utf-8") as f:
            raw = json.load(f)
        return normalize_taxonomy(raw)
    return DEFAULT_TAXONOMY


def tokenize_text(text):
    """Split text into lowercase tokens for keyword matching."""
    if not text:
        return set()
    # Split on non-alphanumeric, keep hyphens within words
    tokens = re.findall(r"[a-z0-9]+(?:-[a-z0-9]+)*", text.lower())
    return set(tokens)


def extract_plugin_tokens(plugin):
    """Extract all searchable tokens from a plugin entry."""
    tokens = set()
    tokens.update(tokenize_text(plugin.get("name", "")))
    tokens.update(tokenize_text(plugin.get("description", "")))
    for tag in plugin.get("tags", []):
        tokens.update(tokenize_text(tag))
    # Also include the category field itself
    tokens.update(tokenize_text(plugin.get("category", "")))
    return tokens


CATEGORY_ALIASES = {
    "testing": "testing-quality",
    "security": "security-compliance",
    "ml-ai": "ai-llm-integration",
    "mobile-development": "mobile-crossplatform",
    "project-management": "productivity-workflow",
    "communication": "communication-collaboration",
    "api-integrations": "ai-llm-integration",
    "version-control": "devops-deployment",
}


def map_plugin_to_categories(plugin, taxonomy_categories):
    """Map a single plugin to taxonomy categories using keyword heuristics.

    Returns a set of category paths (e.g., "code-generation/scaffolding").
    """
    tokens = extract_plugin_tokens(plugin)
    matched_categories = set()

    for token in tokens:
        if token in KEYWORD_CATEGORY_MAP:
            cat_path = KEYWORD_CATEGORY_MAP[token]
            top_cat = cat_path.split("/")[0]
            # Direct match
            if top_cat in taxonomy_categories:
                matched_categories.add(cat_path)
            # Alias match
            elif top_cat in CATEGORY_ALIASES:
                aliased = CATEGORY_ALIASES[top_cat]
                if aliased in taxonomy_categories:
                    new_path = aliased + cat_path[len(top_cat):]
                    matched_categories.add(new_path)

    return matched_categories


def build_plugin_category_index(plugins, taxonomy_categories):
    """Build a mapping of plugin_id -> set of matched category paths."""
    index = {}
    for plugin in plugins:
        plugin_id = plugin.get("id", plugin.get("name", "unknown"))
        categories = map_plugin_to_categories(plugin, taxonomy_categories)
        if categories:
            index[plugin_id] = categories
    return index


def build_category_plugin_index(plugin_cat_index):
    """Invert the plugin->categories index to category->plugins."""
    cat_index = {}
    for plugin_id, categories in plugin_cat_index.items():
        for cat_path in categories:
            if cat_path not in cat_index:
                cat_index[cat_path] = []
            cat_index[cat_path].append(plugin_id)
    return cat_index


def generate_gap_suggestion(category_id, subcategory_id, category_desc, subcategory_desc):
    """Generate an actionable suggestion for a gap."""
    if subcategory_desc:
        return f"Build or find a plugin that provides {subcategory_desc.lower()} capabilities in the {category_id} domain."
    return f"Build or find a plugin that addresses {category_desc.lower()}."


def compute_persona_coverage(persona, taxonomy_categories, category_plugin_index):
    """Compute coverage breakdown for a single persona."""
    covered = []
    partial = []
    gaps = []

    relevant_cats = persona.get("priority_categories", persona.get("relevant_categories", []))

    for cat_id in relevant_cats:
        if cat_id not in taxonomy_categories:
            continue

        cat_info = taxonomy_categories[cat_id]
        subcategories = cat_info.get("subcategories", {})

        # Collect all plugins matching this category or any subcategory
        cat_plugins = set()

        # Direct category match (no subcategory specified)
        if cat_id in category_plugin_index:
            cat_plugins.update(category_plugin_index[cat_id])

        # Subcategory matches
        for sub_id in subcategories:
            full_path = f"{cat_id}/{sub_id}"
            if full_path in category_plugin_index:
                cat_plugins.update(category_plugin_index[full_path])

        plugin_count = len(cat_plugins)
        top_plugins = sorted(cat_plugins)[:5]

        entry = {
            "category": cat_id,
            "description": cat_info.get("description", ""),
            "plugin_count": plugin_count,
            "top_plugins": top_plugins,
        }

        if plugin_count >= 3:
            covered.append(entry)
        elif plugin_count >= 1:
            partial.append(entry)
        else:
            entry["suggestion"] = generate_gap_suggestion(
                cat_id, None, cat_info.get("description", ""), None
            )
            gaps.append(entry)

    return {"covered": covered, "partial": partial, "gaps": gaps}


def compute_category_coverage(taxonomy_categories, category_plugin_index):
    """Compute detailed coverage statistics per taxonomy category."""
    result = {}

    for cat_id, cat_info in taxonomy_categories.items():
        subcategories = cat_info.get("subcategories", {})

        # Total plugins for this category (including subcategories)
        all_plugins = set()
        if cat_id in category_plugin_index:
            all_plugins.update(category_plugin_index[cat_id])

        subcategory_breakdown = {}
        for sub_id, sub_desc in subcategories.items():
            full_path = f"{cat_id}/{sub_id}"
            sub_plugins = category_plugin_index.get(full_path, [])
            all_plugins.update(sub_plugins)
            subcategory_breakdown[sub_id] = {
                "description": sub_desc,
                "plugin_count": len(sub_plugins),
                "plugins": sorted(sub_plugins)[:10],
            }

        result[cat_id] = {
            "description": cat_info.get("description", ""),
            "total_plugins": len(all_plugins),
            "subcategory_breakdown": subcategory_breakdown,
        }

    return result


def compute_cross_plugin_matrix(plugin_cat_index, category_plugin_index, max_plugins=200):
    """Compute overlap and complement relationships between plugins.

    Limited to top plugins by coverage breadth to keep output manageable.
    """
    # Sort plugins by number of categories covered (most versatile first)
    sorted_plugins = sorted(
        plugin_cat_index.items(),
        key=lambda x: len(x[1]),
        reverse=True,
    )[:max_plugins]

    matrix = {}

    for plugin_id, categories in sorted_plugins:
        covers = sorted(categories)

        # Find complementary plugins (cover categories we don't)
        complement_scores = {}
        overlap_scores = {}

        for other_id, other_cats in plugin_cat_index.items():
            if other_id == plugin_id:
                continue
            overlap = categories & other_cats
            unique_other = other_cats - categories

            if overlap and unique_other:
                complement_scores[other_id] = len(unique_other)
            elif overlap and not unique_other:
                overlap_scores[other_id] = len(overlap)

        # Top complements and overlaps
        complements = sorted(
            complement_scores.keys(),
            key=lambda x: complement_scores[x],
            reverse=True,
        )[:5]
        overlaps = sorted(
            overlap_scores.keys(),
            key=lambda x: overlap_scores[x],
            reverse=True,
        )[:5]

        matrix[plugin_id] = {
            "covers": covers,
            "complements": complements,
            "overlaps_with": overlaps,
        }

    return matrix


def recommend_stack(persona_id, taxonomy=None, plugins=None):
    """Recommend the top 5-8 plugins for a given persona.

    Args:
        persona_id: The persona identifier (e.g., "frontend-developer")
        taxonomy: Optional taxonomy dict. Loads from file/default if None.
        plugins: Optional list of plugin dicts. Loads from file if None.

    Returns:
        List of dicts with plugin_id, name, relevance_score, and matched_categories.
    """
    if taxonomy is None:
        taxonomy = load_taxonomy()
    if plugins is None:
        plugins = load_plugins()

    personas = taxonomy.get("personas", {})
    categories = taxonomy.get("categories", {})

    if persona_id not in personas:
        available = list(personas.keys())
        raise ValueError(
            f"Unknown persona '{persona_id}'. Available: {available}"
        )

    persona = personas[persona_id]
    relevant_cats = set(persona.get("priority_categories", persona.get("relevant_categories", [])))

    # Score each plugin by how many relevant categories it covers
    plugin_scores = []

    for plugin in plugins:
        plugin_id = plugin.get("id", plugin.get("name", "unknown"))
        matched = map_plugin_to_categories(plugin, categories)

        # Count matches against persona's relevant categories
        relevance = 0
        matched_relevant = []
        for cat_path in matched:
            top_cat = cat_path.split("/")[0]
            if top_cat in relevant_cats:
                relevance += 1
                matched_relevant.append(cat_path)

        if relevance > 0:
            # Boost score for quality and stars
            quality_bonus = (plugin.get("quality_score", 50) or 50) / 100.0
            stars_bonus = min((plugin.get("github_stars", 0) or 0) / 10000.0, 1.0)
            final_score = relevance + (quality_bonus * 0.5) + (stars_bonus * 0.3)

            plugin_scores.append({
                "plugin_id": plugin_id,
                "name": plugin.get("name", plugin_id),
                "relevance_score": round(final_score, 2),
                "matched_categories": sorted(set(matched_relevant)),
                "quality_score": plugin.get("quality_score"),
                "provider": plugin.get("provider", "unknown"),
            })

    # Sort by relevance score descending, take top 8
    plugin_scores.sort(key=lambda x: x["relevance_score"], reverse=True)

    # Deduplicate: prefer higher-scored entry if same plugin appears
    seen = set()
    results = []
    for entry in plugin_scores:
        if entry["plugin_id"] not in seen:
            seen.add(entry["plugin_id"])
            results.append(entry)
        if len(results) >= 8:
            break

    return results


# ---------------------------------------------------------------------------
# Main Execution
# ---------------------------------------------------------------------------

def run_analysis():
    """Run the full gap analysis and write output."""
    print("Loading plugins...")
    plugins = load_plugins()
    print(f"  Loaded {len(plugins)} plugins")

    print("Loading taxonomy...")
    taxonomy = load_taxonomy()
    categories = taxonomy.get("categories", {})
    personas = taxonomy.get("personas", {})
    print(f"  {len(categories)} categories, {len(personas)} personas")

    print("Mapping plugins to taxonomy categories...")
    plugin_cat_index = build_plugin_category_index(plugins, categories)
    print(f"  {len(plugin_cat_index)} plugins matched to at least one category")

    category_plugin_index = build_category_plugin_index(plugin_cat_index)
    print(f"  {len(category_plugin_index)} category paths have coverage")

    print("Computing persona coverage...")
    persona_coverage = {}
    for persona_id, persona_info in personas.items():
        persona_coverage[persona_id] = compute_persona_coverage(
            persona_info, categories, category_plugin_index
        )
        covered_count = len(persona_coverage[persona_id]["covered"])
        partial_count = len(persona_coverage[persona_id]["partial"])
        gap_count = len(persona_coverage[persona_id]["gaps"])
        print(f"  {persona_id}: {covered_count} covered, {partial_count} partial, {gap_count} gaps")

    print("Computing category coverage...")
    category_coverage = compute_category_coverage(categories, category_plugin_index)

    print("Computing cross-plugin matrix...")
    cross_plugin_matrix = compute_cross_plugin_matrix(plugin_cat_index, category_plugin_index)
    print(f"  {len(cross_plugin_matrix)} plugins in matrix")

    print("Generating recommendations...")
    recommendations = {}
    for persona_id in personas:
        stack = recommend_stack(persona_id, taxonomy=taxonomy, plugins=plugins)
        recommendations[persona_id] = stack
        print(f"  {persona_id}: {len(stack)} recommended plugins")

    # Assemble output
    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_plugins": len(plugins),
            "plugins_with_category_match": len(plugin_cat_index),
            "taxonomy_categories": len(categories),
            "personas_analyzed": len(personas),
        },
        "persona_coverage": persona_coverage,
        "category_coverage": category_coverage,
        "cross_plugin_matrix": cross_plugin_matrix,
        "recommendations": recommendations,
    }

    print(f"\nWriting output to {OUTPUT_PATH}...")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("Done.")
    return output


if __name__ == "__main__":
    run_analysis()
