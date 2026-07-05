# Product Strategy: TripAdvisor for AI Agent Plugins

## 1. Vision

This platform helps developers and knowledge workers find the right AI plugins by organizing them around outcomes, not categories. The AI plugin ecosystem is exploding — thousands of MCP servers, Claude Code skills, Cursor extensions, Copilot plugins — but discovery is broken. You're left scrolling through GitHub awesome-lists or category trees hoping something fits. We flip that model. Like TripAdvisor for restaurants, where you don't search "Italian food category" but "best dinner spot for a date night downtown," this platform lets you say "I need to ship a SaaS MVP this week with auth, payments, and deployment" and get back an opinionated stack of plugins that covers that use case, with clear gaps highlighted and trust signals from real practitioners.

## 2. Core Differentiators

**Use-case-driven discovery.** Users describe what they're trying to accomplish in natural language. The platform maps intent to plugin stacks, not the other way around. No one wakes up thinking "I need a category:databases plugin" — they think "I need to stop writing boilerplate SQL for my API."

**AI-powered gap analysis.** Every use case has a coverage model. When you select a stack, we show what's covered AND what's missing. "Your DevOps stack handles CI/CD and monitoring but has no secrets management or incident response." This is the feature no awesome-list can replicate.

**Multi-tool portability.** Plugins don't live in one ecosystem anymore. A single MCP server might work in Claude Code, Cursor, Copilot, Gemini CLI, and Codex. We track compatibility across tools and surface it as a first-class signal so users aren't locked in.

**Review-gated listing with trust signals.** Not every plugin deserves equal visibility. We surface maintenance activity, install counts, community reviews, and verified compatibility. Abandoned repos sink; actively maintained, well-reviewed plugins rise.

**Cross-plugin stack building with coverage visualization.** Users assemble plugin stacks interactively, watching coverage bars fill in real time. The visual feedback makes gaps obvious and encourages complete coverage rather than piecemeal adoption.

**Persona-driven curation.** A security engineer and a startup founder have fundamentally different needs. Persona lenses reshape the entire experience — what's featured, how things are ranked, which gaps are flagged.

## 3. Personas

### Knowledge Worker

I spend my days in documents, spreadsheets, and Slack threads. I'm not a developer — I don't want to touch a terminal if I can avoid it. But I keep hearing about "AI agents" that can automate the repetitive parts of my job: summarizing meeting notes, filing things in the right place, keeping my second brain up to date. My frustration is that every tool I find assumes I know what an MCP server is or how to edit a JSON config. I'd come back to this platform if it gave me plain-English recipes: "Install these three things and your meeting notes will automatically land in Obsidian, tagged and cross-referenced."

### Web Developer

I'm shipping features in React and Next.js, usually on tight sprint cycles. My stack changes every six months. I need plugins that help me scaffold components, handle state management boilerplate, run lighthouse audits, and preview deploys — but I've been burned by plugins that conflict with each other or don't work past the demo. What would make me return is seeing real compatibility data (does this actually work with Next.js 15?) and honest reviews from people shipping production apps, not just toy demos.

### Backend Engineer

My world is APIs, databases, message queues, and keeping things running at 3 AM. I care about reliability above cleverness. I want plugins that help me generate migration scripts, write integration tests, debug query performance, and manage infrastructure-as-code. My frustration is wading through plugins that look polished but break on anything beyond a hello-world schema. Show me what's battle-tested, show me what pairs well together, and show me what gap in my stack is going to bite me at 2x scale.

### Mobile Developer

I'm dealing with the pain of cross-platform development — React Native or Flutter on one side, platform-specific APIs on the other. Build systems are fragile, simulators are slow, and every OS update breaks something. I need plugins that handle code generation for platform bridges, automate store submissions, and manage device-specific testing. I'd come back if the platform acknowledged that mobile is a different world — not everything that works in VS Code works in Xcode, and I need to know that upfront.

### DevOps Engineer

I automate everything. If I'm doing something twice, it should be a pipeline. I manage infrastructure across multiple clouds, orchestrate deployments, and get paged when things break. I need plugins for Terraform generation, Kubernetes manifest management, CI/CD optimization, and incident response automation. My frustration is that most plugin directories don't understand that my tools chain together — I don't want isolated utilities, I want a stack that covers the full deploy-monitor-respond loop. Show me the coverage map.

### Data Scientist

My days alternate between exploratory notebooks and production ML pipelines. I'm juggling experiment tracking, feature engineering, model serving, and data quality checks. I need plugins that understand the difference between "quick exploration" and "production-ready pipeline." What frustrates me is that dev-focused tools assume I care about clean architecture when I'm just trying to validate a hypothesis, while data-focused tools assume I never need to ship. Give me persona-appropriate recommendations — exploration mode vs. production mode — and I'll keep coming back.

### Security Engineer

I live in audit logs, vulnerability scanners, and compliance frameworks. Everything is a risk assessment. I need plugins for SAST/DAST automation, secrets detection, dependency scanning, and compliance-as-code generation. My frustration is trust — I can't install random community plugins into environments that process sensitive data without knowing who maintains them, what permissions they request, and whether they've been audited. This platform earns my return visits by being the one place that takes supply-chain security of plugins seriously: verified authors, permission transparency, maintenance signals.

### Startup Founder

I wear every hat. I'm writing code in the morning, doing sales calls at lunch, and debugging prod at night. My engineering team is me plus maybe one other person. I need plugins that multiply my output — full-stack scaffolding, auth that just works, payment integration, deployment automation. I don't have time to evaluate fifteen options; I want the opinionated "if you're building a B2B SaaS, install these seven plugins and you're covered." My frustration is that most resources assume I have a team to delegate research to. Give me the curated stack and let me ship.

## 4. Information Architecture

### Landing Page
The entry point asks "What are you building?" with a natural language search bar front and center. Below it: trending use cases as clickable cards (e.g., "Ship a SaaS MVP," "Automate DevOps pipeline," "Build a second brain"), top-rated new plugins, and persona quick-links that reshape the experience.

### Use Case View
Each use case is presented as a recipe — a recommended plugin stack with a coverage bar showing what percentage of the use case is addressed. Gaps are explicitly called out with suggested plugins or a "nothing exists yet" marker. Plugins are ordered by role in the workflow, not alphabetically. Users can swap individual plugins and watch coverage update.

### Plugin Detail
A plugin's page shows: description, author trust signals (maintenance cadence, star history, verified status), reviews from real users with use-case tags, a compatibility matrix (Claude Code / Cursor / Copilot / Gemini CLI / Codex), "pairs well with" recommendations, install instructions per tool, and a changelog summary.

### Stack Builder
An interactive workspace where users assemble plugin stacks. Coverage visualization updates live as plugins are added or removed. Gaps are highlighted. The stack can be exported as a configuration file for the user's tool of choice (Claude Code settings.json, Cursor config, etc.). Shareable stack URLs let teams align on tooling.

## 5. Data Model

### Plugin
Core entity representing a single installable plugin or MCP server. Fields: id, name, description, author, repository_url, install_instructions (per tool), category, subcategories, personas (which personas benefit), keywords, maintenance_score, star_count, last_updated, verified_status, permissions_requested.

### UseCase
A named outcome that users want to achieve. Fields: id, title, description, persona_affinity (which personas most need this), required_capabilities (what the use case demands), recommended_stack (ordered list of plugin IDs), coverage_score (how well the recommended stack covers the use case), gaps (capabilities with no good plugin match).

### Review
User-submitted evaluation of a plugin in context. Fields: id, plugin_id, user_id, use_case_id (which use case they were pursuing), rating, body, tool_used (which AI tool they used it in), verified_install (boolean), created_at, helpful_votes.

### Taxonomy
Hierarchical classification system. Fields: id, category, subcategory, description, keywords (for matching), persona_weights (how relevant to each persona), parent_id (for hierarchy). Currently 12 categories with 60 subcategories mapped to 8 personas.

### Compatibility
Per-plugin, per-tool verification record. Fields: id, plugin_id, tool (claude_code | cursor | copilot | gemini_cli | codex), status (verified | reported_working | untested | known_broken), last_tested, tester_id, notes.

## 6. Current State vs Roadmap

### Built (v0.1)

- **Plugin ingestion pipeline** — `scripts/ingest_plugins.py` pulls from GitHub sources, normalizes metadata, deduplicates, and writes to `catalog.json` (1,121 plugins indexed)
- **12-category taxonomy** with 60 subcategories and 8 persona mappings defined in `taxonomy.json`
- **Gap analysis engine** — `scripts/gap_analysis.py` maps plugins against use-case capabilities using keyword matching, outputs coverage scores and explicit gap lists
- **Frontend** — persona cards for filtered browsing, searchable plugin grid, detail modals with metadata, coverage bars showing category fill rates
- **Static export** — `docs/` contains the deployable SPA hosted on GitHub Pages

### Built (v0.2) — Live

- **Use-case-driven navigation** — 41 use cases in `use_cases.json` powering "What are you building?" hero entry point with click-through recipe views (pain, steps, success criteria, recommended plugins)
- **Premium UI overhaul** — TripAdvisor-style hero, use-case pills, persona grid, trending row, progressive disclosure; purple/orange design system with Inter typeface
- **Natural language search** — autocomplete matches use cases (🎯 shown first) and plugins; Enter navigates to full results page with use-case matches at top, plugin count, sort controls (relevance/stars/name/quality)
- **Global stack builder** — "+" button on every plugin card adds to a persistent stack; nav badge shows count; slide-in drawer lists items with remove buttons; Export copies markdown to clipboard; stack persists in `localStorage`
- **Review system** — seeded ratings for 20 popular plugins (`reviews.json`); aggregate star rating on card footers; full review cards in modal with author, date, verified badge, and rating
- **Multi-tool compatibility** — 5-platform compat matrix (Claude, Cursor, Copilot, Gemini, Codex) on every card and modal
- **Dark mode** — CSS variable system with both explicit toggle and system-preference auto-detection; all components including stack drawer, reviews, and search results are dark-mode aware

### Future (v0.3+)

- **Live review submission** — user-submitted reviews with use-case tagging, moderation pipeline, and verified-install badge earned through install confirmation
- **Multi-tool portability verification** — automated testing of plugins across Claude Code, Cursor, Copilot, Gemini CLI, and Codex
- **Community contribution flow** — plugin authors submit listings, community votes surface quality; claimed listings get analytics dashboard
- **API for programmatic access** — enables integrations, custom dashboards, and third-party tooling
- **"Compare stacks" feature** — side-by-side stack comparison showing coverage differences, cost, and complexity trade-offs
- **Persona evolution** — user behavior refines persona models over time, enabling personalized recommendations
- **Shareable stack URLs** — export stacks as a deep link so teams can align on tooling without sharing config files

## 7. Design Principles

**1. Outcome over category.** Every design decision prioritizes "what are you trying to accomplish" over "what shelf does this sit on." Categories exist as backend metadata, not as primary navigation.

**2. Opinionated curation over exhaustive listing.** We'd rather recommend 5 plugins confidently than list 50 neutrally. Curation is the product. If everything is surfaced equally, we've failed.

**3. Show the gaps, not just the fills.** Most directories celebrate what exists. We also surface what's missing — that's where the actionable insight lives. A gap identified is a problem half-solved.

**4. Trust through transparency.** Every signal is visible: when was this last updated, who reviewed it, does it actually work in your tool, what permissions does it request. No black-box rankings.

**5. Portability matters.** The AI tool landscape is fragmenting. Users shouldn't be punished for switching from Claude Code to Cursor or running both. Plugin recommendations should travel with the user, not lock them in.
