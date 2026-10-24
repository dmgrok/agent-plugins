# Agent Plugins

**Web-based discovery for AI agent plugins.** Browse curated plugins from official and community providers, build your stack, and install it with one script. The badges below show the live counts from the daily catalog build.

[![Plugins](https://img.shields.io/endpoint?url=https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/badge-skills.json)](https://dmgrok.github.io/agent-plugins/)
[![Providers](https://img.shields.io/endpoint?url=https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/badge-providers.json)](https://dmgrok.github.io/agent-plugins/)
[![Quality Tracked](https://img.shields.io/endpoint?url=https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/badge-quality.json)](https://dmgrok.github.io/agent-plugins/)
[![Tests](https://github.com/dmgrok/agent-plugins/actions/workflows/tests.yml/badge.svg)](https://github.com/dmgrok/agent-plugins/actions/workflows/tests.yml)

**[Browse all plugins →](https://dmgrok.github.io/agent-plugins/)**

---

## How It Works

Plugins already live on marketplaces — you just need to find the right ones. This site organizes them around your role and real activities so you can see exactly what coverage you'd get.

1. **Pick your persona** — Web Dev, DevOps, Data Scientist, Security Engineer, and more
2. **Build a stack** — see which of your activities have plugin coverage (Capability Map), add plugins to your stack
3. **Install** — copy the install script and paste it into your terminal

### Install a single plugin

Add this catalog as a Claude Code marketplace once:

```bash
claude plugin marketplace add https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/catalog.json
```

Then every plugin has a copy button. The command is:

```bash
claude plugin install <plugin-name>
```

### Install your whole stack

Click **Copy Install Script** in the Stack Builder. It produces the marketplace line followed by one install line per plugin in your stack:

```bash
claude plugin marketplace add https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/catalog.json
claude plugin install <first-plugin>
claude plugin install <second-plugin>
```

Paste and run. Done.

---

## Providers

Plugins are aggregated from every provider configured in [`scripts/aggregate.py`](scripts/aggregate.py); the Providers badge above shows the current count.

**[View all providers →](https://dmgrok.github.io/agent-plugins/)**

### Featured

| Provider | Repository | Stars |
|----------|-----------|-------|
| [Anthropic](https://github.com/anthropics/skills) | anthropics/skills | ⭐ 54K+ |
| [Obra Superpowers](https://github.com/obra/superpowers) | obra/superpowers | ⭐ 37K+ |
| [GitHub Copilot](https://github.com/github/awesome-copilot) | github/awesome-copilot | ⭐ 19K+ |
| [Vercel](https://github.com/vercel-labs/agent-skills) | vercel-labs/agent-skills | ⭐ 16K+ |
| [VoltAgent](https://github.com/VoltAgent/awesome-agent-skills) | voltagent/awesome-agent-skills | ⭐ 5K+ |
| [NotebookLM](https://github.com/PleasePrompto/notebooklm-skill) | notebooklm-skill | ⭐ 2K+ |
| [OpenAI Codex](https://github.com/openai/skills) | openai/skills | ⭐ 2K+ |
| [heilcheng](https://github.com/heilcheng/awesome-agent-skills) | heilcheng/awesome-agent-skills | ⭐ 1K+ |
| [HuggingFace](https://github.com/huggingface/skills) | huggingface/skills | ⭐ 1K+ |
| [Playwright](https://github.com/lackeyjb/playwright-skill) | playwright-skill | ⭐ 1K+ |

### Enterprise & Official

Stripe · Cloudflare · Supabase · Trail of Bits · Expo · Sentry · Google Labs Stitch · Better Auth · Tinybird · Neon Database · fal.ai · Remotion · nginity

### Community

SkillCreator.ai · iOS Simulator · Claude Marketplace · CSV Summarizer · Tapestry Skills · AWS Skills · FFUF Web Fuzzing · D3.js Visualization · EPUB Converter · Sanjay AI Skills · PICT Test Cases · Family History · Move Code Quality

---

## Quality System

Every skill gets a quality score (0–100) based on three factors:

| Factor | Max Points | Details |
|--------|-----------|---------|
| **Maintenance** | 50 | 🟢 Active (&lt;30d) = 50 · 🟡 Maintained (&lt;6mo) = 40 · 🟠 Stale (&lt;1yr) = 20 · 🔴 Abandoned = 5 |
| **Documentation** | 30 | Scripts (+10) · References (+10) · Assets (+10) |
| **Provider Trust** | 20 | Official = 20 · Community = 10 |

---

## API & Exports

The catalog is updated daily at 06:00 UTC and available via CDN:

```
https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/catalog.json
```

Pre-filtered exports for specific ecosystems:

| Export | Filter | URL |
|--------|--------|-----|
| Claude Skills | Quality ≥ 50 | [`exports/claude-skills.json`](https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/claude-skills.json) |
| Copilot Skills | Quality ≥ 50 | [`exports/copilot-skills.json`](https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/copilot-skills.json) |
| Premium Skills | Quality ≥ 70 | [`exports/premium-skills.json`](https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/premium-skills.json) |
| Active Skills | Updated &lt; 6mo | [`exports/active-skills.json`](https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/active-skills.json) |
| MCP-Compatible | Tagged `mcp` | [`exports/mcp-compatible.json`](https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/exports/mcp-compatible.json) |

```python
import requests
catalog = requests.get(
    "https://cdn.jsdelivr.net/gh/dmgrok/agent-plugins@main/catalog.json"
).json()

quality_skills = [s for s in catalog["skills"] if s["quality_score"] >= 80]
```

---

## Plugins Listing

<!-- AUTO-GENERATED SKILLS TABLE START -->
## 📋 All Skills — 1318 skills across 48 providers · v2026.10.24

> Auto-generated daily · [Browse interactively →](https://dmgrok.github.io/agent-plugins/)  
> Legend: 🔒 Secrets scan · 🛡️ Injection check · 📝 Content · 🔄 No duplicate · ✅ Full skill · S=Scripts · R=References · A=Assets

| Skill | Provider | Compat | 🔒 | 🛡️ | 📝 | 🔄 | ✅ | S | R | A | Quality | Status | Dup |
|-------|----------|--------|----|----|----|----|---|---|---|---|---------|--------|-----|
| [microsoft-store-publisher](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/microsoft-store-publisher/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 100/100 | 🟢 active |  |
| [openai-docs](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/openai-docs/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 100/100 | 🟢 active |  |
| [openai-docs](https://raw.githubusercontent.com/openai/skills/main/skills/.system/openai-docs/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 100/100 | 🟢 active | 🔄 → openai/openai-docs |
| [acquire-codebase-knowledge](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/acquire-codebase-knowledge/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [agent-memory](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agent-memory/skills/agent-memory/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [agent-regression-evals](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agent-regression-evals/skills/agent-regression-evals/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [agent-regression-evals](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/agent-regression-evals/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active | 🔄 → nginity/agent-regression-evals |
| [agile-product-owner](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/agile-product-owner/skills/agile-product-owner/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [app-store-optimization](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/app-store-optimization/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [azure-architecture-autopilot](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-architecture-autopilot/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [bug-receipt](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/bug-receipt/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [capacity-planner](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/capacity-planner/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [channel-economics](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/channel-economics/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [chaos-engineering](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/chaos-engineering/skills/chaos-engineering/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [chaos-engineering](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/chaos-engineering/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active | 🔄 → nginity/chaos-engineering |
| [clinical-research](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research-ops/skills/clinical-research/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [coding-agent-rollout](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/coding-agent-rollout/skills/coding-agent-rollout/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [coding-agent-rollout](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/coding-agent-rollout/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active | 🔄 → nginity/coding-agent-rollout |
| [commercial-forecaster](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/commercial-forecaster/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [commercial-policy](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/commercial-policy/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [compliance-os](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/compliance-os/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [copilot-pr-autopilot](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/copilot-pr-autopilot/SKILL.md) | github | Copilot | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [cypress-flake-fixer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/cypress-flake-fixer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 90/100 | 🟢 active |  |
| [daily-focus-board](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/daily-focus-board/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [deal-desk](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/deal-desk/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [design-system](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/markdown-html/skills/design-system/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [diagramming-code](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/diagramming-code/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [excalidraw-diagram-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/excalidraw-diagram-generator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [expo-ui](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-ui/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 90/100 | 🟢 active |  |
| [feature-flags-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/feature-flags-architect/skills/feature-flags-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [feature-flags-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/feature-flags-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active | 🔄 → nginity/feature-flags-architect |
| [figma-code-connect-components](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma-code-connect-components/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [figma-create-design-system-rules](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma-create-design-system-rules/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [figma-generate-library](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma-generate-library/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [geofeed-tuner](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/geofeed-tuner/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [imagegen](https://raw.githubusercontent.com/openai/skills/main/skills/.system/imagegen/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [internal-comms](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/internal-comms/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [interpreting-culture-index](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/culture-index/skills/interpreting-culture-index/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [jupyter-notebook](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/jupyter-notebook/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [knowledge-ops](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/knowledge-ops/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [kubernetes-operator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/kubernetes-operator/skills/kubernetes-operator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [kubernetes-operator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/kubernetes-operator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active | 🔄 → nginity/kubernetes-operator |
| [let-fate-decide](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/let-fate-decide/skills/let-fate-decide/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [linkedin-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing/linkedin/skills/linkedin-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [llm-wiki](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/llm-wiki/skills/llm-wiki/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [make-blog-post](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/make-blog-post/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [market-research](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research-ops/skills/market-research/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [md-document](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/markdown-html/skills/md-document/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [md-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/markdown-html/skills/md-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [md-slides](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/markdown-html/skills/md-slides/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [meetings](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/meetings/skills/meetings/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [month-end-close](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/month-end-close/skills/month-end-close/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [month-end-close](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/skills/month-end-close/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active | 🔄 → nginity/month-end-close |
| [partnerships-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/partnerships-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [playwright](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/playwright/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [pm-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/pm-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [pricing-strategist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/pricing-strategist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [process-mapper](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/process-mapper/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [procurement-optimizer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/procurement-optimizer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [product-research](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research-ops/skills/product-research/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [product-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/product-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [research-finance](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research-ops/skills/research-finance/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [rfp-responder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/rfp-responder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [roast](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/roast/skills/roast/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [semgrep](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/static-analysis/skills/semgrep/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [session-handoff](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/handoff/skills/session-handoff/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [skill-installer](https://raw.githubusercontent.com/openai/skills/main/skills/.system/skill-installer/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 90/100 | 🟢 active |  |
| [slo-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/slo-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [slo-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/slo-architect/skills/slo-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active | 🔄 → nginity/slo-architect |
| [social-media-analyzer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/social-media-analyzer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [speech](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/speech/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [supabase](https://raw.githubusercontent.com/supabase/agent-skills/main/skills/supabase/SKILL.md) | supabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [trailmark-finding-triage](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/trailmark-finding-triage/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [transcribe](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/transcribe/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟡 maintained |  |
| [turnstile-spin](https://raw.githubusercontent.com/cloudflare/skills/main/skills/turnstile-spin/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 90/100 | 🟢 active |  |
| [vendor-management](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/vendor-management/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [verification-agent](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/verification-agent/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [weekly-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/weekly-review/skills/weekly-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [yara-rule-authoring](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/yara-authoring/skills/yara-rule-authoring/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 90/100 | 🟢 active |  |
| [a11y-audit](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/a11y-audit/skills/a11y-audit/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [adobe-illustrator-scripting](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/adobe-illustrator-scripting/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [agent-harness](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agent-harness/skills/agent-harness/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [agent-skill-stack](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/agent-skill-stack/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [agenthub](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/agenthub/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [agents-sdk](https://raw.githubusercontent.com/cloudflare/skills/main/skills/agents-sdk/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [andreessen](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/andreessen/skills/andreessen/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [apple-hig-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/apple-hig-expert/skills/apple-hig-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [arkit-visionos-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/arkit-visionos-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [arquiteto-de-empresa](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/arquiteto-de-empresa/skills/arquiteto-de-empresa/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [arquiteto-de-empresa](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/arquiteto-de-empresa/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained | 🔄 → nginity/arquiteto-de-empresa |
| [aspnet-core](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/aspnet-core/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [atlassian-admin](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/atlassian-admin/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [audit-integrity](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/audit-integrity/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [autoresearch-agent](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/autoresearch-agent/skills/autoresearch-agent/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [aws-cdk-development](https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/aws-iac/skills/aws-cdk-development/SKILL.md) | aws-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [aws-solution-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/aws-solution-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [basin](https://raw.githubusercontent.com/cloudflare/skills/main/skills/basin/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [batch-files](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/batch-files/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [batch-script-progress](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/batch-script-progress/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [board-meeting](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/board-meeting/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [book-to-skill](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/book-to-skill/skills/book-to-skill/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [build-evidence-map](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/build-evidence-map/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [campaign-analytics](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/campaign-analytics/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [capa-officer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/capa-officer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [capture](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/capture/skills/capture/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [caveman](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/caveman/skills/caveman/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [changelog-generator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/changelog-generator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [character-design](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/character-design/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [chatgpt-apps](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/chatgpt-apps/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [chief-ai-officer-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/chief-ai-officer-advisor/skills/chief-ai-officer-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [chief-ai-officer-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/chief-ai-officer-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active | 🔄 → nginity/chief-ai-officer-advisor |
| [chief-data-officer-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/chief-data-officer-advisor/skills/chief-data-officer-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [chief-data-officer-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/chief-data-officer-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active | 🔄 → nginity/chief-data-officer-advisor |
| [cinematography](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/cinematography/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [claude-coach](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/claude-coach/skills/claude-coach/SKILL.md) | nginity | Claude | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [cloudflare](https://raw.githubusercontent.com/cloudflare/skills/main/skills/cloudflare/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [cloudflare-deploy](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/cloudflare-deploy/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [cloudflare-email-service](https://raw.githubusercontent.com/cloudflare/skills/main/skills/cloudflare-email-service/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [code-to-prd](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/code-to-prd/skills/code-to-prd/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [codeql](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/static-analysis/skills/codeql/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [coding-standards-enforcer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/coding-standards-enforcer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [commercial](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/commercial/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [commit-message-storyteller](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/commit-message-storyteller/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [connect-recommend](https://raw.githubusercontent.com/stripe/ai/main/skills/connect-recommend/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [content-production](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/content-production/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [convert-excel-to-md](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/convert-excel-to-md/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [convert-pdf-to-md](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/convert-pdf-to-md/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [convert-word-to-md](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/convert-word-to-md/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [create-quarkus-project](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-quarkus-project/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [cs-onboard](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/cs-onboard/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [customer-success-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-growth/skills/customer-success-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [d365-solution-blueprint](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/d365-solution-blueprint/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [decision-logger](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/decision-logger/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [deep-learning-book](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/deep-learning-book/skills/deep-learning-book/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [deep-work](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/deep-work/skills/deep-work/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [dependency-auditor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/dependency-auditor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [diagnosing-superpowers](https://raw.githubusercontent.com/obra/superpowers/main/skills/diagnosing-superpowers/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [dimensional-analysis](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/dimensional-analysis/skills/dimensional-analysis/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [durable-objects](https://raw.githubusercontent.com/cloudflare/skills/main/skills/durable-objects/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [eas-app-stores](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/eas-app-stores/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [eas-observe](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/eas-observe/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [eas-simulator](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/eas-simulator/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [eas-update-insights](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/eas-update-insights/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [eas-workflows](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/eas-workflows/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 80/100 | 🟢 active |  |
| [entry-point-analyzer](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/entry-point-analyzer/skills/entry-point-analyzer/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [eu-ai-act-specialist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/compliance-team-eu-ai-act/skills/eu-ai-act-specialist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [eu-ai-act-specialist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/eu-ai-act-specialist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active | 🔄 → nginity/eu-ai-act-specialist |
| [expo-app-clip](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-app-clip/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-brownfield](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-brownfield/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-data-fetching](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-data-fetching/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-design-system](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-design-system/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-examples](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-examples/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-migrate-module](https://raw.githubusercontent.com/expo/skills/main/plugins/expo-experiments/skills/expo-migrate-module/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-module](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-module/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-native-ui](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-native-ui/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-overview](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-overview/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-router](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-router/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-upgrade](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-upgrade/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [expo-web-to-native](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-web-to-native/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [fal-models-catalog](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/fal-models-catalog/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [fal-prompting](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/fal-prompting/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [fal-recipes](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/fal-recipes/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [fan-cam](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/fan-cam/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [figma](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [figma-use](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma-use/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [financial-analyst](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/skills/financial-analyst/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [firebase-apk-scanner](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/firebase-apk-scanner/skills/firebase-apk-scanner/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [foundry-hosted-agent-copilotkit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/foundry-hosted-agent-copilotkit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [general-counsel-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/general-counsel-advisor/skills/general-counsel-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [general-counsel-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/general-counsel-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active | 🔄 → nginity/general-counsel-advisor |
| [genmedia](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/genmedia/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [genmedia-workflow](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/genmedia-workflow/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [gh-fix-ci](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/gh-fix-ci/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 80/100 | 🟡 maintained |  |
| [google-workspace-cli](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/google-workspace-cli/skills/google-workspace-cli/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [graph-evolution](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/graph-evolution/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [grill-me](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/grill-me/skills/grill-me/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [grill-with-docs](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/grill-with-docs/skills/grill-with-docs/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [handoff](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/handoff/skills/handoff/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [hatch-pet](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/hatch-pet/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [hf-cloud-sagemaker-iam-preflight](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-cloud-sagemaker-iam-preflight/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [hf-cloud-sagemaker-production-defaults](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-cloud-sagemaker-production-defaults/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [hf-cloud-serving-image-selection](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-cloud-serving-image-selection/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [hivemind](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/hivemind/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [human-gate](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/human-gate/skills/human-gate/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [incident-commander](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/incident-commander/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [interview-mapper](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research-ops/skills/interview-mapper/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [interview-system-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/interview-system-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [isms-audit-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/isms-audit-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-add-graalvm-native-image-support](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-add-graalvm-native-image-support/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-debugging](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-debugging/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-development](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-development/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-diagnostics](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-diagnostics/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-hibernate-jpa](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-hibernate-jpa/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-junit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-junit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-testcontainers](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-testcontainers/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [java-upgrade](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-upgrade/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [karpathy-coder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/karpathy-coder/skills/karpathy-coder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [landing-page-generator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/landing-page-generator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [linkedin-analytics](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing/linkedin/skills/linkedin-analytics/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [linkedin-content](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing/linkedin/skills/linkedin-content/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [linkedin-engagement](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing/linkedin/skills/linkedin-engagement/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [linkedin-profile](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing/linkedin/skills/linkedin-profile/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [linkedin-strategy](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing/linkedin/skills/linkedin-strategy/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [lsp-setup](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/lsp-setup/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [markdown-html-orchestrator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/markdown-html/skills/markdown-html-orchestrator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [marketing](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/marketing/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [marketing-demand-acquisition](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/marketing-demand-acquisition/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [mdr-745-specialist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/mdr-745-specialist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [memory-engineering](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/memory-engineering/skills/memory-engineering/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [mermaid-to-proverif](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/mermaid-to-proverif/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [migrate-to-codex](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/migrate-to-codex/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [migration-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/migration-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [mini-context-graph](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mini-context-graph/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [neon](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [neon-functions](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-functions/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [neon-postgres](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-postgres/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [neon-realtime](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-realtime/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [netlify-deploy](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/netlify-deploy/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [observability-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/observability-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [passive-deal-screener](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/skills/passive-deal-screener/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [plugin-creator](https://raw.githubusercontent.com/openai/skills/main/skills/.system/plugin-creator/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [poka-yoke](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/poka-yoke/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [pr-dashboard](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pr-dashboard/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 80/100 | 🟡 maintained |  |
| [product-manager-toolkit](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/product-manager-toolkit/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [product-strategist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/product-strategist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [pulse](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/pulse/skills/pulse/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [python-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/python-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [qms-audit-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/qms-audit-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [quality-documentation-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/quality-documentation-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [quality-manager-qmr](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/quality-manager-qmr/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [quality-manager-qms-iso13485](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/quality-manager-qms-iso13485/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [quarkus-application-development](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/quarkus-application-development/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [realitykit-visionos-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/realitykit-visionos-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [regulatory-affairs-head](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/regulatory-affairs-head/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [remotion-best-practices](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-best-practices/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-captions](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-captions/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-create](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-create/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-docs](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-docs/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-interactivity](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-interactivity/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-maps](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-maps/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-markup](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-markup/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-multimedia](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-multimedia/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-render](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-render/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-saas](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-saas/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-studio](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-studio/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [remotion-upgrade](https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion-upgrade/SKILL.md) | remotion | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 80/100 | 🟢 active |  |
| [render-deploy](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/render-deploy/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [revenue-operations](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-growth/skills/revenue-operations/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [roslyn-analyzers](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/roslyn-analyzers/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [saas-metrics-coach](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/skills/saas-metrics-coach/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [sales-engineer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-growth/skills/sales-engineer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [sample-text-processor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/skill-tester/assets/sample-skill/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [sandbox-next](https://raw.githubusercontent.com/cloudflare/skills/main/skills/sandbox-next/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [screenshot](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/screenshot/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 80/100 | 🟡 maintained |  |
| [scrum-master](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/scrum-master/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [security-model](https://raw.githubusercontent.com/getsentry/skills/main/skills/security-model/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [security-ownership-map](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/security-ownership-map/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [senior-backend](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-backend/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [senior-frontend](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-frontend/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [senior-fullstack](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-fullstack/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [senior-ml-engineer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-ml-engineer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [senior-pm](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/senior-pm/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [senior-qa](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-qa/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [shadergraph-editor](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/shadergraph-editor/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [shareplay-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/shareplay-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [skill-creator](https://raw.githubusercontent.com/openai/skills/main/skills/.system/skill-creator/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [skill-doctor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skill-doctor/skills/skill-doctor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [skill-scanner](https://raw.githubusercontent.com/getsentry/skills/main/skills/skill-scanner/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [skill-tester](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/skill-tester/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [slicing-code-context](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/slicing-code-context/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [spatial-swiftui-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/spatial-swiftui-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [storytelling](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/storytelling/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [stripe-apps](https://raw.githubusercontent.com/stripe/ai/main/skills/stripe-apps/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [stripe-best-practices](https://raw.githubusercontent.com/stripe/ai/main/skills/stripe-best-practices/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [subagent-driven-development](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [swiftui-chart3d-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/swiftui-chart3d-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [tdd-guide](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/tdd-guide/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [tech-debt-tracker](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/tech-debt-tracker/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [tech-stack-evaluator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/tech-stack-evaluator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [trailmark](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/trailmark/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [train-sentence-transformers](https://raw.githubusercontent.com/huggingface/skills/main/skills/train-sentence-transformers/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [ugc](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/ugc/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [ui-design-system](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/ui-design-system/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [usd-editor](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/usd-editor/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [usdkit-runtime-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/usdkit-runtime-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [ux-researcher-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/ux-researcher-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [vercel-deploy](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/vercel-deploy/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 80/100 | 🟡 maintained |  |
| [vercel-optimize](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/vercel-optimize/SKILL.md) | vercel | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟡 maintained |  |
| [vercel-react-view-transitions](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-view-transitions/SKILL.md) | vercel | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [visionos-immersive-media-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/visionos-immersive-media-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [visionos-widgetkit-developer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/visionos-widgetkit-developer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [vpe-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/vpe-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [vpe-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/vpe-advisor/skills/vpe-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active | 🔄 → nginity/vpe-advisor |
| [webinar-marketing](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/webinar-marketing/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [webmcpify](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/webmcpify/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [winui-app](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/winui-app/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [workers-best-practices](https://raw.githubusercontent.com/cloudflare/skills/main/skills/workers-best-practices/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [workflow-builder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/workflow-builder/skills/workflow-builder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 80/100 | 🟡 maintained |  |
| [write-a-skill](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/write-a-skill/skills/write-a-skill/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 80/100 | 🟢 active |  |
| [zeroize-audit](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/zeroize-audit/skills/zeroize-audit/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 80/100 | 🟢 active |  |
| [ab-test-setup](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/ab-test-setup/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [ad-creative](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/ad-creative/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [aeo](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/aeo/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [agent-architecture](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/agent-architecture/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [agent-decision-receipts](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/agent-decision-receipts/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [agent-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/agent-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [agent-launcher-orchestrator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/agent-launcher/skills/agent-launcher-orchestrator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [agent-protocol](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/agent-protocol/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [agent-workflow-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/agent-workflow-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [agentic-actions-auditor](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/agentic-actions-auditor/skills/agentic-actions-auditor/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [ai-security](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/ai-security/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [ai-team-orchestration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ai-team-orchestration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [analytics-tracking](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/analytics-tracking/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [anti-ui-slop](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/anti-ui-slop/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [api-design-reviewer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/api-design-reviewer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [apple-appstore-reviewer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/apple-appstore-reviewer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [arduino-azure-iot-edge-integration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arduino-azure-iot-edge-integration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-ai-provider-integration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-ai-provider-integration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-annotation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-annotation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-dataset](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-dataset/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-evaluator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-evaluator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-experiment](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-experiment/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-instrumentation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-instrumentation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-link](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-link/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-prompt-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-prompt-optimization/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arize-trace](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arize-trace/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [arkit-camera-access-providers](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/arkit-camera-access-providers/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟢 active |  |
| [arkit-hand-tracking-provider](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/arkit-hand-tracking-provider/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟢 active |  |
| [arkit-reference-tracking-providers](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/arkit-reference-tracking-providers/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟢 active |  |
| [arkit-rendering-context-providers](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/arkit-rendering-context-providers/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟢 active |  |
| [arkit-spatial-tracking-providers](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/arkit-spatial-tracking-providers/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟢 active |  |
| [atlassian-templates](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/atlassian-templates/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [audit-augmentation](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/audit-augmentation/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [aws-agentic-ai](https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/aws-agentic-ai/skills/aws-agentic-ai/SKILL.md) | aws-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [aws-sst-development](https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/aws-iac/skills/aws-sst-development/SKILL.md) | aws-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [azure-cloud-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/azure-cloud-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [azure-container-registry-cli](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-container-registry-cli/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [azure-developer-cli](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-developer-cli/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [azure-devops-cli](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-devops-cli/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [azure-smart-city-iot-solution-builder](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-smart-city-iot-solution-builder/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [better-auth-best-practices](https://raw.githubusercontent.com/better-auth/skills/main/better-auth/best-practices/SKILL.md) | better-auth | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [board-deck-builder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/board-deck-builder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [brainiall-diarized-transcription](https://raw.githubusercontent.com/fasuizu-br/brainiall-transcription-skill/main/skills/brainiall-diarized-transcription/SKILL.md) | brainiall | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [brainstorming](https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [browser-automation](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/browser-automation/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [burpsuite-project-parser](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/burpsuite-project-parser/skills/burpsuite-project-parser/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [ceo-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/ceo-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [cf-cli](https://raw.githubusercontent.com/cloudflare/skills/main/skills/cf-cli/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [cfo-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/cfo-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [chief-customer-officer-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/chief-customer-officer-advisor/skills/chief-customer-officer-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [chief-customer-officer-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/chief-customer-officer-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained | 🔄 → nginity/chief-customer-officer-advisor |
| [chro-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/chro-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [chrome-mcp-troubleshooting](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/chrome-mcp-troubleshooting/skills/chrome-mcp-troubleshooting/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟢 active |  |
| [churn-prevention](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/churn-prevention/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [ci-cd-pipeline-builder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/ci-cd-pipeline-builder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [ciso-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/ciso-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [claude-api](https://raw.githubusercontent.com/anthropics/skills/main/skills/claude-api/SKILL.md) | anthropics | Claude | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [cli-creator](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/cli-creator/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [cloud-security](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/cloud-security/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [cloudflare-one](https://raw.githubusercontent.com/cloudflare/skills/main/skills/cloudflare-one/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [cloudflare-one-migrations](https://raw.githubusercontent.com/cloudflare/skills/main/skills/cloudflare-one-migrations/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [cmo-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/cmo-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [code-reviewer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/code-reviewer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [codebase-memory-mcp](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/codebase-memory-mcp/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [codebase-onboarding](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/codebase-onboarding/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [cold-email](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/cold-email/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [competitive-intel](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/competitive-intel/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [competitive-teardown](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/competitive-teardown/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [competitor-alternatives](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/competitor-alternatives/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [confluence-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/confluence-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [connect-required-verification-information](https://raw.githubusercontent.com/stripe/ai/main/skills/connect-required-verification-information/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [constant-time-analysis](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/constant-time-analysis/skills/constant-time-analysis/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [content-creator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/content-creator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [content-humanizer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/content-humanizer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [content-management-systems](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/content-management-systems/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [content-strategy](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/content-strategy/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [context-engine](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/context-engine/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [conventional-branch](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/conventional-branch/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [coo-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/coo-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [copy-editing](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/copy-editing/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [copywriting](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/copywriting/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [cpo-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/cpo-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [create-auth](https://raw.githubusercontent.com/better-auth/skills/main/better-auth/create-auth/SKILL.md) | better-auth | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [creating-oracle-to-postgres-migration-bug-report](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/creating-oracle-to-postgres-migration-bug-report/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [cro-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/cro-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [cto-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/cto-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [culture-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/culture-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [data-breach-blast-radius](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/data-breach-blast-radius/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [data-quality-auditor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/data-quality-auditor/skills/data-quality-auditor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [database-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/database-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [dependabot](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dependabot/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [devcontainer-setup](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/devcontainer-setup/skills/devcontainer-setup/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [django-access-review](https://raw.githubusercontent.com/getsentry/skills/main/skills/django-access-review/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [doc-and-modernize](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/doc-and-modernize/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [docker-development](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/docker-development/skills/docker-development/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [docs-sync-audit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/docs-sync-audit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [docx](https://raw.githubusercontent.com/anthropics/skills/main/skills/docx/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [dossier](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/dossier/skills/dossier/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [dotnet-mcp-builder](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dotnet-mcp-builder/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [draw-io-diagram-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/draw-io-diagram-generator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 70/100 | 🟠 stale |  |
| [drawio](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/drawio/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [eas-hosting](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/eas-hosting/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [eas-update](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/eas-update/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [efcore-d2-db-diagram](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/efcore-d2-db-diagram/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [email-and-password-best-practices](https://raw.githubusercontent.com/better-auth/skills/main/better-auth/emailAndPassword/SKILL.md) | better-auth | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [email-sequence](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/email-sequence/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [emblem-ai-agent-wallet](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-ai-agent-wallet/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [env-secrets-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/env-secrets-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [epic-design](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/epic-design/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [eval-driven-dev](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/eval-driven-dev/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [executing-plans](https://raw.githubusercontent.com/obra/superpowers/main/skills/executing-plans/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [executive-mentor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/executive-mentor/skills/executive-mentor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [experiment-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/experiment-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [expo-animation](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-animation/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [expo-dev-client](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-dev-client/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [expo-dom](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-dom/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [expo-project-structure](https://raw.githubusercontent.com/expo/skills/main/plugins/expo/skills/expo-project-structure/SKILL.md) | expo | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [fable-goal](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/fable-goal/skills/fable-goal/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [fal-gamedev](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/fal-gamedev/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [fal-redesign](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/fal-redesign/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [fal-regenerate-3d](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/fal-regenerate-3d/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [fda-consultant-specialist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/fda-consultant-specialist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [figma-create-new-file](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma-create-new-file/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [figma-generate-design](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma-generate-design/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [figma-implement-design](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/figma-implement-design/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [flowstudio-power-automate-build](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/flowstudio-power-automate-build/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [flowstudio-power-automate-debug](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/flowstudio-power-automate-debug/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [flowstudio-power-automate-mcp](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/flowstudio-power-automate-mcp/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [form-cro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/form-cro/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [fp-check](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/fp-check/skills/fp-check/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [free-tool-strategy](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/free-tool-strategy/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [gateway-workers](https://raw.githubusercontent.com/cloudflare/skills/main/skills/gateway-workers/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [gcp-cloud-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/gcp-cloud-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [gdpr-dsgvo-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/gdpr-dsgvo-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [genotoxic](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/genotoxic/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [gha-security-review](https://raw.githubusercontent.com/getsentry/skills/main/skills/gha-security-review/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [git-commit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/git-commit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [git-worktree-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/git-worktree-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [github-actions-efficiency](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/github-actions-efficiency/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [github-actions-hardening](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/github-actions-hardening/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [github-codespaces-efficiency](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/github-codespaces-efficiency/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [github-issues](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/github-issues/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [github-release](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/github-release/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [github-triage](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/github-triage/skills/github-triage/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [gitmoji](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gitmoji/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [google-chat](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/google-chat/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [grade-iterate](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/agent-launcher/skills/grade-iterate/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [grants](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/grants/skills/grants/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [helm-chart-builder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/helm-chart-builder/skills/helm-chart-builder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [hf-cli](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-cli/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [hf-cloud-python-env-setup](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-cloud-python-env-setup/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [huggingface-lora-space-builder](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-lora-space-builder/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [huggingface-paper-publisher](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-paper-publisher/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 70/100 | 🟠 stale |  |
| [huggingface-spaces](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-spaces/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [huggingface-trackio](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-trackio/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [huggingface-zerogpu](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-zerogpu/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [impediment-prioritization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/impediment-prioritization/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [inbox-setup](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/email/skills/inbox-setup/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [inbox-triage](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/email/skills/inbox-triage/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [incident-response](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/incident-response/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [information-security-manager-iso27001](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/information-security-manager-iso27001/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [internal-narrative](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/internal-narrative/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [interview](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/agent-launcher/skills/interview/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [ios-simulator-skill](https://raw.githubusercontent.com/conorluddy/ios-simulator-skill/main/ios-simulator-skill/skills/ios-simulator-skill/SKILL.md) | ios-simulator-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [iso42001-specialist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/compliance-team-iso42001/skills/iso42001-specialist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [iso42001-specialist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/iso42001-specialist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained | 🔄 → nginity/iso42001-specialist |
| [java-docs](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-docs/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [java-refactoring-extract-method](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-refactoring-extract-method/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [java-refactoring-remove-parameter](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-refactoring-remove-parameter/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [javax-to-jakarta-migration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/javax-to-jakarta-migration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [jira-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/jira-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [k2](https://raw.githubusercontent.com/cloudflare/skills/main/skills/k2/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [landing](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing/landing/skills/landing/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [latchshot-page-capture](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/latchshot-page-capture/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [launch-strategy](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/launch-strategy/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [lean-comments](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/lean-comments/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [linear](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/linear/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [litreview](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/litreview/skills/litreview/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [local-seo-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/local-seo-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [macos-golden-gate-design](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/macos-golden-gate-design/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [marketing-context](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/marketing-context/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [marketing-ops](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/marketing-ops/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [marketing-strategy-pmm](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/marketing-strategy-pmm/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [markstream-install](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/markstream-install/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [mcp-security-audit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-security-audit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [mcp-server-builder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/mcp-server-builder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [md-to-docx](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/md-to-docx/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [metronome](https://raw.githubusercontent.com/stripe/ai/main/skills/metronome/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [minecraft-plugin-development](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/minecraft-plugin-development/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [model-routing](https://raw.githubusercontent.com/fal-ai-community/skills/main/skills/model-routing/SKILL.md) | fal-ai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [monorepo-navigator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/monorepo-navigator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [ms365-tenant-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/ms365-tenant-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [msgraph-sdk](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/msgraph-sdk/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [mutation-testing](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/mutation-testing/skills/mutation-testing/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [mvvm-toolkit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mvvm-toolkit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [mvvm-toolkit-di](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mvvm-toolkit-di/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [mvvm-toolkit-messenger](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mvvm-toolkit-messenger/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [namecheap](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/namecheap/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [napkin](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/napkin/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [neon-ai-gateway](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-ai-gateway/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [neon-auth](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-auth/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [neon-object-storage](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-object-storage/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [nextjs-on-cloudflare](https://raw.githubusercontent.com/cloudflare/skills/main/skills/nextjs-on-cloudflare/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [notebooklm](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/notebooklm/skills/notebooklm/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [npm-trusted-publishing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/npm-trusted-publishing/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [open-sourcing](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/open-sourcing/skills/open-sourcing/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [optimize-simplicite-logs](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/optimize-simplicite-logs/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [org-health-diagnostic](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/org-health-diagnostic/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [organization-best-practices](https://raw.githubusercontent.com/better-auth/skills/main/better-auth/organization/SKILL.md) | better-auth | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [paid-ads](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/paid-ads/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [patent](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/patent/skills/patent/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [pdf](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/pdf/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [performance-profiler](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/performance-profiler/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [pester-migration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pester-migration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [pester-should-migration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pester-should-migration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [phoenix-cli](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/phoenix-cli/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [phoenix-evals](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/phoenix-evals/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [phoenix-tracing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/phoenix-tracing/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [playwright-interactive](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/playwright-interactive/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [playwright-pro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/pw/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [post-patch-validation](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/post-patch-validation/skills/post-patch-validation/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [pptx](https://raw.githubusercontent.com/anthropics/skills/main/skills/pptx/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [pr-address-feedback](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pr-address-feedback/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [pricing-strategy](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/pricing-strategy/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [product-analytics](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/product-analytics/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [product-discovery](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/product-discovery/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [prompt-engineer-toolkit](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/prompt-engineer-toolkit/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [property-based-testing](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/property-based-testing/skills/property-based-testing/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [protobuf-grpc-api-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/protobuf-grpc-api-review/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [python-azure-iot-edge-modules](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/python-azure-iot-edge-modules/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [quality-playbook](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/quality-playbook/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [quarkus-dev-services-and-testing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/quarkus-dev-services-and-testing/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [quarkus-native-and-container](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/quarkus-native-and-container/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [react-container-presentation-component](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react-container-presentation-component/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [realitykit-animation-physics](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/realitykit-animation-physics/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [realitykit-audio-spatial](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/realitykit-audio-spatial/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [realitykit-ecs-systems](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/realitykit-ecs-systems/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [realitykit-rendering-materials](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/realitykit-rendering-materials/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [rebase-current-branch](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/rebase-current-branch/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [red-green-proof](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/red-green-proof/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [red-team](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/red-team/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [referral-program](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/referral-program/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [reflect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/reflect/skills/reflect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [repo-standardizer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/repo-standardizer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [research](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/research/skills/research/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [research-summarizer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/research-summarizer/skills/research-summarizer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [resemble-detect](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/resemble-detect/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [reviewing-oracle-to-postgres-migration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/reviewing-oracle-to-postgres-migration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [rhino3d-scripts](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/rhino3d-scripts/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [risk-management-specialist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/risk-management-specialist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [roadmap-communicator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/roadmap-communicator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [run-without-you](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/agent-launcher/skills/run-without-you/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [runbook-generator](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/runbook-generator/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [saas-scaffolder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/saas-scaffolder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [sandbox-migrate-to-next](https://raw.githubusercontent.com/cloudflare/skills/main/skills/sandbox-migrate-to-next/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [sandbox-stable](https://raw.githubusercontent.com/cloudflare/skills/main/skills/sandbox-stable/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [scenario-war-room](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/scenario-war-room/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [schema-markup](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/schema-markup/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [second-opinion](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/second-opinion/skills/second-opinion/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [secret-serialization](https://raw.githubusercontent.com/getsentry/skills/main/skills/secret-serialization/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [secrets-vault-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/secrets-vault-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [security-best-practices](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/security-best-practices/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [security-pen-testing](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/security-pen-testing/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [security-review](https://raw.githubusercontent.com/getsentry/skills/main/skills/security-review/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [security-threat-model](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/security-threat-model/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [semgrep-rule-creator](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/semgrep-rule-creator/skills/semgrep-rule-creator/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [semgrep-rule-variant-creator](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/semgrep-rule-variant-creator/skills/semgrep-rule-variant-creator/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [senior-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [senior-computer-vision](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-computer-vision/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [senior-data-engineer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-data-engineer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [senior-data-scientist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-data-scientist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [senior-devops](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-devops/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [senior-prompt-engineer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-prompt-engineer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [senior-secops](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-secops/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [senior-security](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/senior-security/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [sentry](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/sentry/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [seo-audit](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/seo-audit/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [setup-my-iq](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/setup-my-iq/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [sharp-edges](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/sharp-edges/skills/sharp-edges/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [ship-gate](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/ship-gate/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [signup-flow-cro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/signup-flow-cro/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [site-architecture](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/site-architecture/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [skill-creator](https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 70/100 | 🟠 stale |  |
| [skill-security-auditor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/skill-security-auditor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [skill-writer](https://raw.githubusercontent.com/getsentry/skills/main/skills/skill-writer/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [slang-shader-engineer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/slang-shader-engineer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [snowflake-development](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/snowflake-development/skills/snowflake-development/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [soc2-compliance](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/soc2-compliance/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [speak-summary](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/speak-summary/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [spec-driven-workflow](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/spec-driven-workflow/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [spec-to-repo](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/product-team/skills/spec-to-repo/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [sql-database-assistant](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/sql-database-assistant/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [sql-server-table-reconciliation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/sql-server-table-reconciliation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [stage-launch](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/agent-launcher/skills/stage-launch/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [statistical-analyst](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/statistical-analyst/skills/statistical-analyst/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [stock-analysis](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/skills/stock-analysis/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [strategic-alignment](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/strategic-alignment/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [stripe-directory](https://raw.githubusercontent.com/stripe/ai/main/skills/stripe-directory/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [stripe-pay](https://raw.githubusercontent.com/stripe/ai/main/skills/stripe-pay/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [stripe-projects](https://raw.githubusercontent.com/stripe/ai/main/skills/stripe-projects/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [supabase-postgres-best-practices](https://raw.githubusercontent.com/supabase/agent-skills/main/skills/supabase-postgres-best-practices/SKILL.md) | supabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [supply-chain-risk-auditor](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/supply-chain-risk-auditor/skills/supply-chain-risk-auditor/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [syllabus](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/syllabus/skills/syllabus/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [tc-tracker](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/tc-tracker/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [terraform-patterns](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/terraform-patterns/skills/terraform-patterns/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [test-gap-audit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/test-gap-audit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [threat-detection](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/threat-detection/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [tm7-threat-model](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/tm7-threat-model/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [trailmark-review-gate](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/trailmark-review-gate/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [trailmark-variant-neighborhood](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/trailmark-variant-neighborhood/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [triage-frontend-issues](https://raw.githubusercontent.com/getsentry/skills/main/skills/triage-frontend-issues/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [trl-training](https://raw.githubusercontent.com/huggingface/skills/main/skills/trl-training/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [two-factor-authentication-best-practices](https://raw.githubusercontent.com/better-auth/skills/main/better-auth/twoFactor/SKILL.md) | better-auth | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [universal-scraping-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/universal-scraping-architect/skills/universal-scraping-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [upgrade-stripe](https://raw.githubusercontent.com/stripe/ai/main/skills/upgrade-stripe/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [v-development](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/v-development/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [variant-analysis](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/variant-analysis/skills/variant-analysis/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [vcpkg](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/vcpkg/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [vector-forge](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/vector-forge/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 70/100 | 🟡 maintained |  |
| [web-design-reviewer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/web-design-reviewer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [whatsapp](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/whatsapp/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [workers-profiling](https://raw.githubusercontent.com/cloudflare/skills/main/skills/workers-profiling/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [wrangler](https://raw.githubusercontent.com/cloudflare/skills/main/skills/wrangler/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [wrap-up](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/agent-launcher/skills/wrap-up/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟢 active |  |
| [writing-skills](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 70/100 | 🟢 active |  |
| [x-twitter-growth](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/x-twitter-growth/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 70/100 | 🟡 maintained |  |
| [xlsx](https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 70/100 | 🟡 maintained |  |
| [yeet](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/yeet/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 70/100 | 🟡 maintained |  |
| [academy-guide](https://raw.githubusercontent.com/anthropics/skills/main/skills/academy-guide/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [acreadiness-assess](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/acreadiness-assess/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [acreadiness-generate-instructions](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/acreadiness-generate-instructions/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [acreadiness-policy](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/acreadiness-policy/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [ad-campaign-analyzer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ad-campaign-analyzer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [address-sanitizer](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/address-sanitizer/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [adjudicate-regression](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/regression-hunt/skills/adjudicate-regression/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [adversarial-reviewer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/adversarial-reviewer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [aflpp](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/aflpp/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [ai-act-readiness](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/ai-act-readiness/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [ai-ready](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ai-ready/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [aims-audit](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/aims-audit/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [algorand-vulnerability-scanner](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/algorand-vulnerability-scanner/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [api-breaking-change-detector](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/api-breaking-change-detector/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [api-test-suite-builder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/api-test-suite-builder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [appinsights-instrumentation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/appinsights-instrumentation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [apple-container](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/apple-container/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [ar-resume](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/autoresearch-agent/skills/ar-resume/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [ar-run](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/autoresearch-agent/skills/ar-run/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [ar-status](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/autoresearch-agent/skills/ar-status/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [atheris](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/atheris/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [audit-context-building](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/audit-context-building/skills/audit-context-building/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [audit-prep-assistant](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/audit-prep-assistant/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [aws-cloudwatch-investigation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aws-cloudwatch-investigation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [aws-cost-operations](https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/aws-cost-ops/skills/aws-cost-operations/SKILL.md) | aws-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [aws-cost-optimize](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aws-cost-optimize/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [aws-resource-health-diagnose](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aws-resource-health-diagnose/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [aws-resource-query](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aws-resource-query/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [aws-serverless-eda](https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/serverless-eda/skills/aws-serverless-eda/SKILL.md) | aws-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [aws-well-architected-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aws-well-architected-review/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [azure-well-architected-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-well-architected-review/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [behuman](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/behuman/skills/behuman/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [bench-read](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/bench-read/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [best-practices](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/best-practices/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [board](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/board/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [boardroom](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/boardroom/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [boost-asio-pro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/boost-asio-pro/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [brag-sheet](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/brag-sheet/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [brand-guidelines](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/brand-guidelines/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [breakdown-feature-implementation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/breakdown-feature-implementation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [brief](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/brief/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [bug-reproduction-brief](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/bug-reproduction-brief/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [business-growth-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-growth/skills/business-growth-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [business-name-fit](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/business-name-fit/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [business-operations-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-operations/skills/business-operations-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [c-level-agents](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/c-level-agents/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [c-level-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/c-level-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [caio-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/caio-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [cairo-vulnerability-scanner](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/cairo-vulnerability-scanner/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [cargo-fuzz](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/cargo-fuzz/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [cco-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cco-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [cdo-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cdo-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [cfo-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cfo-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [change-management](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/change-management/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [chief-of-staff](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/chief-of-staff/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [ciso-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/ciso-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [claude-settings-audit](https://raw.githubusercontent.com/getsentry/skills/main/skills/claude-settings-audit/SKILL.md) | getsentry | Claude | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [cmo-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cmo-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [code-maturity-assessor](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/code-maturity-assessor/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [code-tour](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/code-tour/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [collab-proof](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/collab-proof/skills/collab-proof/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [commercial-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/commercial/skills/commercial-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [commitments](https://raw.githubusercontent.com/maxbaluev/accreted-intelligence/main/plugins/claude/skills/commitments/SKILL.md) | accint | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [company-os](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/company-os/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [competitor-ad-intelligence](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/competitor-ad-intelligence/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [compliance-readiness](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/compliance-readiness/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [constant-time-testing](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/constant-time-testing/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [copilot-sdk](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/copilot-sdk/SKILL.md) | github | Copilot | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [coverage-analysis](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/coverage-analysis/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [cpo-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cpo-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [create-implementation-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-implementation-plan/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [create-specification](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-specification/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [create-spring-boot-java-project](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-spring-boot-java-project/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [create-spring-boot-kotlin-project](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-spring-boot-kotlin-project/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [creating-oracle-to-postgres-master-migration-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/creating-oracle-to-postgres-master-migration-plan/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [creating-oracle-to-postgres-migration-integration-tests](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/creating-oracle-to-postgres-migration-integration-tests/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [cro-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cro-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [cross-eval](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cross-eval/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [cto-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/cto-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [database-schema-designer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/database-schema-designer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [datanalysis-credit-risk](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/datanalysis-credit-risk/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [decide](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/decide/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [deep-research](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/deep-research/skills/deep-research/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [deepread](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research/deepread/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [define-goal](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/define-goal/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [demo-video](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/demo-video/skills/demo-video/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [deploy-to-vercel](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/deploy-to-vercel/SKILL.md) | vercel | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [desk-journal](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/desk-journal/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [desk-open](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/desk-open/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [diagnose](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/diagnose/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [differential-review](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/differential-review/skills/differential-review/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [discernment-nudge](https://raw.githubusercontent.com/anthropics/skills/main/skills/discernment-nudge/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [django-perf-review](https://raw.githubusercontent.com/getsentry/skills/main/skills/django-perf-review/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [dwarf-expert](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/dwarf-expert/skills/dwarf-expert/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [em-dash](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/em-dash/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [embedded-iot-mentor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/embedded-iot-mentor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-ai](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-ai/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-ai-prompt-examples](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-ai-prompt-examples/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-ai-react](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-ai-react/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-defi-yield](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-defi-yield/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-market-research](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-market-research/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-memecoin-scout](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-memecoin-scout/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-portfolio-tracker](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-portfolio-tracker/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [emblem-token-swap](https://raw.githubusercontent.com/EmblemCompany/Agent-skills/main/skills/emblem-token-swap/SKILL.md) | emblemcompany | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [engineering-advanced-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/engineering-advanced-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [engineering-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/engineering-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [eval](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/eval/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [execute](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/execute/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [eyeball](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/eyeball/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [fda-qsr-audit-prep](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/fda-qsr-audit-prep/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [finance-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/skills/finance-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [flowstudio-power-automate-governance](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/flowstudio-power-automate-governance/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [flowstudio-power-automate-monitoring](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/flowstudio-power-automate-monitoring/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [focused-fix](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/focused-fix/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [founder-coach](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/founder-coach/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [founder-mode](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/founder-mode/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [frames](https://raw.githubusercontent.com/maxbaluev/accreted-intelligence/main/plugins/claude/skills/frames/SKILL.md) | accint | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [freeze](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/freeze/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [from-the-other-side-anitta](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/from-the-other-side-anitta/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [from-the-other-side-quinn](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/from-the-other-side-quinn/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [from-the-other-side-wiggins](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/from-the-other-side-wiggins/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [frontend-design](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [full-page-screenshot](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/full-page-screenshot/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [fuzzing-dictionary](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/fuzzing-dictionary/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [fuzzing-obstacles](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/fuzzing-obstacles/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [game-engine](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/game-engine/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 60/100 | 🟠 stale |  |
| [gc-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/gc-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [gdpr-audit-prep](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/gdpr-audit-prep/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [gem-devops-guidelines](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gem-devops-guidelines/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [generate-image](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/generate-image/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [gh-address-comments](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/gh-address-comments/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 60/100 | 🟠 stale |  |
| [gh-attach](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gh-attach/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [gh-cli](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/gh-cli/skills/gh-cli/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [gh-review-requests](https://raw.githubusercontent.com/getsentry/skills/main/skills/gh-review-requests/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [github-actions-runtime-upgrade-conventions](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/github-actions-runtime-upgrade-conventions/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [goal-prompt](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/goal-prompt/skills/goal-prompt/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [grok-build](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/grok-build/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [guidelines-advisor](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/guidelines-advisor/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [harness-engineering](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/harness-engineering/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [harness-writing](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/harness-writing/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [hf-cloud-aws-context-discovery](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-cloud-aws-context-discovery/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [hf-cloud-sagemaker-deployment-planner](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-cloud-sagemaker-deployment-planner/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [hf-mem](https://raw.githubusercontent.com/huggingface/skills/main/skills/hf-mem/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [hub-init](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/hub-init/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [hub-run](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/hub-run/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [hub-status](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/hub-status/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [huggingface-best](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-best/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [huggingface-datasets](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-datasets/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [huggingface-llm-trainer](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-llm-trainer/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [huggingface-vision-trainer](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-vision-trainer/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [hunt-regressions](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/regression-hunt/skills/hunt-regressions/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [image-annotations](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/image-annotations/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [implement-patch](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/patching-bugs/skills/implement-patch/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [incident-postmortem](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/incident-postmortem/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [intl-expansion](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/intl-expansion/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [iso13485-audit-prep](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/iso13485-audit-prep/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [iso27001-audit-prep](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/iso27001-audit-prep/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [iterate-pr](https://raw.githubusercontent.com/getsentry/skills/main/skills/iterate-pr/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [java-helidon](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-helidon/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [landing-page-conversion-audit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/landing-page-conversion-audit/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [learn-this](https://raw.githubusercontent.com/michalparkola/tapestry-skills-for-claude-code/main/learn-this/SKILL.md) | tapestry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [libafl](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/libafl/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [libfuzzer](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/libfuzzer/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [llm-cost-optimizer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/llm-cost-optimizer/skills/llm-cost-optimizer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [loop](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/autoresearch-agent/skills/loop/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [loop-library](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/loop-library/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [ma-playbook](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/skills/ma-playbook/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [markdown-to-epub-converter](https://raw.githubusercontent.com/smerchek/claude-epub-skill/main/markdown-to-epub/SKILL.md) | epub-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [marketing-ideas](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/marketing-ideas/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [marketing-psychology](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/marketing-psychology/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [marketing-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/marketing-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [mcp-builder](https://raw.githubusercontent.com/anthropics/skills/main/skills/mcp-builder/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [mcp-implementation-security-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-implementation-security-review/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [mcp-release-qa](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-release-qa/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [merge](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/merge/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [migrating-oracle-to-postgres-data-access-code](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/migrating-oracle-to-postgres-data-access-code/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [migrating-oracle-to-postgres-stored-procedures](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/migrating-oracle-to-postgres-stored-procedures/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [modern-cpp](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/modern-cpp/skills/modern-cpp/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [named-persona-adversarial-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/named-persona-adversarial-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [nano-banana-pro-openrouter](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/nano-banana-pro-openrouter/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | 60/100 | 🟠 stale |  |
| [neon-postgres-branches](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-postgres-branches/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [neon-postgres-egress-optimizer](https://raw.githubusercontent.com/neondatabase/agent-skills/main/skills/neon-postgres-egress-optimizer/SKILL.md) | neondatabase | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [notion-knowledge-capture](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/notion-knowledge-capture/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 60/100 | 🟠 stale |  |
| [notion-meeting-intelligence](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/notion-meeting-intelligence/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 60/100 | 🟠 stale |  |
| [notion-research-documentation](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/notion-research-documentation/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 60/100 | 🟠 stale |  |
| [notion-spec-to-implementation](https://raw.githubusercontent.com/openai/skills/main/skills/.curated/notion-spec-to-implementation/SKILL.md) | openai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 60/100 | 🟠 stale |  |
| [office-hours](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/office-hours/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [onboard](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/onboard/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [onboarding-cro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/onboarding-cro/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [oo-component-documentation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/oo-component-documentation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 60/100 | 🟠 stale |  |
| [ossfuzz](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/ossfuzz/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [outline](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/outline/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [page-cro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/page-cro/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [patching-bugs](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/patching-bugs/skills/patching-bugs/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [performance-review-writer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/performance-review-writer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [pinecone-rag](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pinecone-rag/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [planning-oracle-to-postgres-migration-integration-testing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/planning-oracle-to-postgres-migration-integration-testing/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [playwright-skill](https://raw.githubusercontent.com/lackeyjb/playwright-skill/main/skills/playwright-skill/SKILL.md) | playwright-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [popup-cro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/popup-cro/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [post-mortem](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/post-mortem/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [pr-screenshots](https://raw.githubusercontent.com/getsentry/skills/main/skills/pr-screenshots/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [pr-screenshots](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pr-screenshots/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [prepare-regression](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/regression-hunt/skills/prepare-regression/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [presentation-creator](https://raw.githubusercontent.com/getsentry/skills/main/skills/presentation-creator/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [programmatic-seo](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/programmatic-seo/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [prompt-optimizer](https://raw.githubusercontent.com/getsentry/skills/main/skills/prompt-optimizer/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [prompt-optimizer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/prompt-optimizer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [prove-patch](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/patching-bugs/skills/prove-patch/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [python-pypi-package-builder](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/python-pypi-package-builder/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [ra-qm-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/ra-qm-team/skills/ra-qm-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [rag-architect](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/rag-architect/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [react19-test-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react19-test-patterns/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [refactor-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/refactor-plan/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [regression-hunt](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/regression-hunt/skills/regression-hunt/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [replay-regression](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/regression-hunt/skills/replay-regression/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [report-regressions](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/regression-hunt/skills/report-regressions/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [reproduce-bug](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/patching-bugs/skills/reproduce-bug/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [reproduce-regression](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/regression-hunt/skills/reproduce-regression/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [requesting-code-review](https://raw.githubusercontent.com/obra/superpowers/main/skills/requesting-code-review/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [research-ops-skills](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/research-ops/skills/research-ops-skills/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [resx-source-generator-migration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/resx-source-generator-migration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [review-walkthrough](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/review-walkthrough/skills/review-walkthrough/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [ruby-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ruby-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [ruzzy](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/ruzzy/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [sarif-parsing](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/static-analysis/skills/sarif-parsing/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [scaffolding-oracle-to-postgres-migration-test-project](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/scaffolding-oracle-to-postgres-migration-test-project/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [screen-recording](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/screen-recording/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [scrum-sage](https://raw.githubusercontent.com/michalparkola/tapestry-skills-for-claude-code/main/scrum-sage/SKILL.md) | tapestry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [secure-workflow-guide](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/secure-workflow-guide/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [security-guidance](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/security-guidance/skills/security-guidance/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [sematext-otel](https://raw.githubusercontent.com/sematext/sematext-otel-onboarding/main/skills/SKILL.md) | sematext | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [server-side-conversion-tracking](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/server-side-conversion-tracking/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [session-log](https://raw.githubusercontent.com/michalparkola/tapestry-skills-for-claude-code/main/session-log/SKILL.md) | tapestry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [setup](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/autoresearch-agent/skills/setup/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [shopify-review-triage](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/shopify-review-triage/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [shotglass](https://raw.githubusercontent.com/jakemanger/shotglass-skills/main/skills/shotglass/SKILL.md) | shotglass | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [signal-write](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/signal-write/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [skillopt-sleep](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skillopt-sleep/skills/skillopt-sleep/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [soc2-audit-prep](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/compliance-os/skills/soc2-audit-prep/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [social-content](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/social-content/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [social-media-manager](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/social-media-manager/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [solana-vulnerability-scanner](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/solana-vulnerability-scanner/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [solve](https://raw.githubusercontent.com/maxbaluev/accreted-intelligence/main/plugins/claude/skills/solve/SKILL.md) | accint | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [spatial-app-architecture](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/spatial-app-architecture/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [spawn](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/agenthub/skills/spawn/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [spec-to-code-compliance](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/spec-to-code-compliance/skills/spec-to-code-compliance/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [spinning-up-deep-rl](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/spinning-up-deep-rl/skills/spinning-up-deep-rl/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [sql-code-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/sql-code-review/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [sql-object-impact-analysis](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/sql-object-impact-analysis/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [sred-project-organizer](https://raw.githubusercontent.com/getsentry/skills/main/skills/sred-project-organizer/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [ssma-console](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ssma-console/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [steno-mode](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/steno-mode/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [stream-coding](https://raw.githubusercontent.com/frmoretto/stream-coding/main/skills/stream-coding/SKILL.md) | stream-coding | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [stripe-docs](https://raw.githubusercontent.com/stripe/ai/main/skills/stripe-docs/SKILL.md) | stripe | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [substrate-vulnerability-scanner](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/substrate-vulnerability-scanner/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [swedish-mentor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/productivity/swedish-mentor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [system-commandline-cli](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/system-commandline-cli/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [systematic-debugging](https://raw.githubusercontent.com/obra/superpowers/main/skills/systematic-debugging/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [team-communications](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/team-communications/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [technical-job-search](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/technical-job-search/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [telegram](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/telegram/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [terraform-azurerm-set-diff-analyzer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/terraform-azurerm-set-diff-analyzer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 60/100 | 🟠 stale |  |
| [testing-handbook-generator](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/testing-handbook-generator/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [tiny-stepping](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/tiny-stepping/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [tinybird](https://raw.githubusercontent.com/tinybirdco/tinybird-agent-skills/main/skills/tinybird-best-practices/SKILL.md) | tinybird | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [tinybird-cli-guidelines](https://raw.githubusercontent.com/tinybirdco/tinybird-agent-skills/main/skills/tinybird-cli-guidelines/SKILL.md) | tinybird | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [tinybird-python-sdk-guidelines](https://raw.githubusercontent.com/tinybirdco/tinybird-agent-skills/main/skills/tinybird-python-sdk-guidelines/SKILL.md) | tinybird | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [tinybird-typescript-sdk-guidelines](https://raw.githubusercontent.com/tinybirdco/tinybird-agent-skills/main/skills/tinybird-typescript-sdk-guidelines/SKILL.md) | tinybird | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [token-integration-analyzer](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/token-integration-analyzer/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [ton-vulnerability-scanner](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/ton-vulnerability-scanner/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [trailmark-structural](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/trailmark-structural/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [trailmark-summary](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/trailmark-summary/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [tugboat](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/tugboat/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [typescript-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/typescript-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [ui-screenshots](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ui-screenshots/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [unblock-action](https://raw.githubusercontent.com/michalparkola/tapestry-skills-for-claude-code/main/unblock-action/SKILL.md) | tapestry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [update-markdown-file-index](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/update-markdown-file-index/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [update-specification](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/update-specification/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [upstash-redis](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/upstash-redis/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [using-superpowers](https://raw.githubusercontent.com/obra/superpowers/main/skills/using-superpowers/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [validate-bug](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/patching-bugs/skills/validate-bug/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [vardoger-analyze](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/vardoger-analyze/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [vercel-cli-with-tokens](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/vercel-cli-with-tokens/SKILL.md) | vercel | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [vercel-react-best-practices](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-best-practices/SKILL.md) | vercel | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [verify-agent-action](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/verify-agent-action/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [vpe-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-agents/skills/vpe-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [vulnerability-triage-brocards](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/vulnerability-triage-brocards/skills/vulnerability-triage-brocards/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [web-perf](https://raw.githubusercontent.com/cloudflare/skills/main/skills/web-perf/SKILL.md) | cloudflare | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [workshop-create](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/workshop-create/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [writing-guidelines](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/writing-guidelines/SKILL.md) | vercel | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [writing-lean-proofs](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/writing-lean-proofs/skills/writing-lean-proofs/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 60/100 | 🟡 maintained |  |
| [writing-plans](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [wycheproof](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/testing-handbook-skills/skills/wycheproof/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 60/100 | 🟡 maintained |  |
| [x-twitter-scraper](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/x-twitter-scraper/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟡 maintained |  |
| [youtube-full](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/youtube-full/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [zero-hallucination-coder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/zero-hallucination-coder/skills/zero-hallucination-coder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 60/100 | 🟢 active |  |
| [agents-md](https://raw.githubusercontent.com/getsentry/skills/main/skills/agents-md/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [ai-decision-authority](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/ai-decision-authority/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [algorithmic-art](https://raw.githubusercontent.com/anthropics/skills/main/skills/algorithmic-art/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 50/100 | 🟠 stale |  |
| [api-testing](https://raw.githubusercontent.com/aiqualitylab/agent-skills/main/skills/api-testing/SKILL.md) | aiqualitylab | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [architecture-diagram-creator](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/visual-documentation-plugin/skills/architecture-diagram-creator/SKILL.md) | claude-marketplace-visual | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 50/100 | 🟠 stale |  |
| [article-extractor](https://raw.githubusercontent.com/michalparkola/tapestry-skills-for-claude-code/main/article-extractor/SKILL.md) | tapestry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [ask-questions-if-underspecified](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/ask-questions-if-underspecified/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [aspire](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aspire/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [audit-library-health](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/audit-library-health/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [aws-mcp-setup](https://raw.githubusercontent.com/zxkane/aws-skills/main/plugins/aws-common/skills/aws-mcp-setup/SKILL.md) | aws-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [azure-deployment-preflight](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-deployment-preflight/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [azure-pricing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-pricing/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [azure-resource-visualizer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-resource-visualizer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 50/100 | 🟠 stale |  |
| [backend-development](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/backend-development/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [board-prep](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/executive-mentor/skills/board-prep/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [browse-and-evaluate](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/browse-and-evaluate/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [browserstack](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/browserstack/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [build-workspace-docs](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/build-workspace-docs/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [business-investment-advisor](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/finance/business-investment-advisor/skills/business-investment-advisor/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [c-review](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/c-review/skills/c-review/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [challenge](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/executive-mentor/skills/challenge/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [changelog-generator](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/changelog-generator/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [cli-mastery](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/cli-mastery/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [cloud-design-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/cloud-design-patterns/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [code-documentation](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/code-documentation/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [code-improver](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/code-improver/skills/code-improver/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [code-tour](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/code-tour/skills/code-tour/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [codeql](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/codeql/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [commit](https://raw.githubusercontent.com/getsentry/skills/main/skills/commit/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [content-research-writer](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/content-research-writer/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [contract-and-proposal-writer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/business-growth/skills/contract-and-proposal-writer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [create-branch](https://raw.githubusercontent.com/getsentry/skills/main/skills/create-branch/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [crypto-protocol-diagram](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/trailmark/skills/crypto-protocol-diagram/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 50/100 | 🟠 stale |  |
| [csv-data-summarizer](https://raw.githubusercontent.com/coffeefuelbump/csv-data-summarizer-claude-skill/main/SKILL.md) | csv-summarizer-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [curate-a-team-library](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/curate-a-team-library/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [d3-viz](https://raw.githubusercontent.com/chrisvoncsefalvay/claude-d3js-skill/main/SKILL.md) | d3js-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [dashboard-creator](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/visual-documentation-plugin/skills/dashboard-creator/SKILL.md) | claude-marketplace-visual | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 50/100 | 🟠 stale |  |
| [database-design](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/database-design/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [dispatching-parallel-agents](https://raw.githubusercontent.com/obra/superpowers/main/skills/dispatching-parallel-agents/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [document-api-endpoint](https://raw.githubusercontent.com/getsentry/skills/main/skills/document-api-endpoint/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [dotnet-timezone](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dotnet-timezone/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [doublecheck](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/doublecheck/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 50/100 | 🟠 stale |  |
| [email-template-builder](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/email-template-builder/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [extract](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/self-improving-agent/skills/extract/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [fabric-lakehouse](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/fabric-lakehouse/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [family-history-planning](https://raw.githubusercontent.com/emaynard/claude-family-history-research-skill/main/SKILL.md) | family-history-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [ffuf-web-fuzzing](https://raw.githubusercontent.com/jthack/ffuf_claude_skill/main/ffuf-skill/SKILL.md) | ffuf-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [finishing-a-development-branch](https://raw.githubusercontent.com/obra/superpowers/main/skills/finishing-a-development-branch/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [finnish-humanizer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/finnish-humanizer/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [flowchart-creator](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/visual-documentation-plugin/skills/flowchart-creator/SKILL.md) | claude-marketplace-visual | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 50/100 | 🟠 stale |  |
| [fluentui-blazor](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/fluentui-blazor/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [freecad-scripts](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/freecad-scripts/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [gdpr-compliant](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gdpr-compliant/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [generate](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/generate/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [gsap-framer-scroll-animation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gsap-framer-scroll-animation/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [hard-call](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/executive-mentor/skills/hard-call/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [huggingface-community-evals](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-community-evals/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 50/100 | 🟠 stale |  |
| [huggingface-local-models](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-local-models/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [huggingface-tool-builder](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-tool-builder/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [install-from-remote-library](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/install-from-remote-library/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [issue-fields-migration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/issue-fields-migration/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [jules](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/jules/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [legacy-circuit-mockups](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/legacy-circuit-mockups/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [linkedin-post-formatter](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/linkedin-post-formatter/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [llm-application-dev](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/llm-application-dev/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [make-repo-contribution](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/make-repo-contribution/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 50/100 | 🟠 stale |  |
| [markdown-to-html](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/markdown-to-html/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [meeting-analyzer](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/project-management/skills/meeting-analyzer/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [memory-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/self-improving-agent/skills/memory-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [memory-status](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/self-improving-agent/skills/memory-status/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [microsoft-agent-framework](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/microsoft-agent-framework/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [microsoft-skill-creator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/microsoft-skill-creator/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [migrate](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/migrate/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [migrate-skills-between-libraries](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/migrate-skills-between-libraries/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [minimalist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/minimalist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [modern-python](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/modern-python/skills/modern-python/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 50/100 | 🟠 stale |  |
| [move-code-quality](https://raw.githubusercontent.com/1NickPappas/move-code-quality-skill/main/SKILL.md) | move-quality-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [noob-mode](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/noob-mode/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [notebooklm](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/notebooklm/SKILL.md) | sanjay-ai-skills | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [panel-review](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/code-improver/tests/fixtures/review-panel/skills/panel-review/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [paywall-upgrade-cro](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/skills/paywall-upgrade-cro/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [pdf](https://raw.githubusercontent.com/anthropics/skills/main/skills/pdf/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 50/100 | 🟠 stale |  |
| [pdftk-server](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pdftk-server/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [penpot-uiux-design](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/penpot-uiux-design/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [pict-test-designer](https://raw.githubusercontent.com/omkamal/pypict-claude-skill/main/SKILL.md) | pypict-skill | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [postmortem](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/executive-mentor/skills/postmortem/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [powerbi-modeling](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/powerbi-modeling/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [pr-improver](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/code-improver/skills/pr-improver/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [pr-link-issue](https://raw.githubusercontent.com/getsentry/skills/main/skills/pr-link-issue/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [pr-review-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/pr-review-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [pr-writer](https://raw.githubusercontent.com/getsentry/skills/main/skills/pr-writer/SKILL.md) | getsentry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [promote](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/self-improving-agent/skills/promote/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [prompt-governance](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/prompt-governance/skills/prompt-governance/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [publish-to-pages](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/publish-to-pages/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 50/100 | 🟠 stale |  |
| [pw-init](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/pw-init/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [pw-review](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/pw-review/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [react-audit-grep-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react-audit-grep-patterns/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react18-batching-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react18-batching-patterns/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react18-dep-compatibility](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react18-dep-compatibility/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react18-enzyme-to-rtl](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react18-enzyme-to-rtl/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react18-legacy-context](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react18-legacy-context/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react18-lifecycle-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react18-lifecycle-patterns/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react18-string-refs](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react18-string-refs/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react19-concurrent-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react19-concurrent-patterns/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [react19-source-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/react19-source-patterns/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [receiving-code-review](https://raw.githubusercontent.com/obra/superpowers/main/skills/receiving-code-review/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [remember](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/self-improving-agent/skills/remember/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [review-a-skill](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/review-a-skill/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [review-pr](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/code-improver/tests/fixtures/pr-review-toolkit/skills/review-pr/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [roundup-setup](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/roundup-setup/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [rust-review](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/rust-review/skills/rust-review/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [sandbox-npm-install](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/sandbox-npm-install/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 50/100 | 🟠 stale |  |
| [secret-scanning](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/secret-scanning/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [security-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/security-review/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [Selenium Self-Healing](https://raw.githubusercontent.com/aiqualitylab/agent-skills/main/skills/selenium-selfhealing/SKILL.md) | aiqualitylab | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [self-eval](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/skills/self-eval/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [self-improving-agent](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/self-improving-agent/skills/self-improving-agent/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [semantic-kernel](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/semantic-kernel/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [share-a-library](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/share-a-library/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [ship-learn-next](https://raw.githubusercontent.com/michalparkola/tapestry-skills-for-claude-code/main/ship-learn-next/SKILL.md) | tapestry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [skill-improver](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/code-improver/skills/skill-improver/SKILL.md) | trailofbits | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [spring-boot-testing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/spring-boot-testing/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [stress-test](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/c-level-advisor/executive-mentor/skills/stress-test/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [strict-api](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering/strict-api/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [stripe-integration-expert](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/skills/stripe-integration-expert/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [technical-doc-creator](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/visual-documentation-plugin/skills/technical-doc-creator/SKILL.md) | claude-marketplace-visual | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 50/100 | 🟠 stale |  |
| [test-driven-development](https://raw.githubusercontent.com/obra/superpowers/main/skills/test-driven-development/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [testrail](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/testrail/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [threat-model-analyst](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/threat-model-analyst/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [timeline-creator](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/visual-documentation-plugin/skills/timeline-creator/SKILL.md) | claude-marketplace-visual | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ✅ | 50/100 | 🟠 stale |  |
| [tkr-skill-writer](https://raw.githubusercontent.com/tomkrikorian/visionOSAgents/main/skills/tkr-skill-writer/SKILL.md) | visionos-agents | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [transformers-js](https://raw.githubusercontent.com/huggingface/skills/main/skills/transformers-js/SKILL.md) | huggingface | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [unit-test-vue-pinia](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/unit-test-vue-pinia/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 50/100 | 🟠 stale |  |
| [update-installed-skills](https://raw.githubusercontent.com/skillcreatorai/Ai-Agent-Skills/main/skills/update-installed-skills/SKILL.md) | skillcreatorai | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [using-git-worktrees](https://raw.githubusercontent.com/obra/superpowers/main/skills/using-git-worktrees/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [verification-before-completion](https://raw.githubusercontent.com/obra/superpowers/main/skills/verification-before-completion/SKILL.md) | obra-superpowers | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [video-content-strategist](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/marketing-skill/video-content-strategist/skills/video-content-strategist/SKILL.md) | nginity | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [web-artifacts-builder](https://raw.githubusercontent.com/anthropics/skills/main/skills/web-artifacts-builder/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 50/100 | 🟠 stale |  |
| [webapp-testing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/webapp-testing/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 50/100 | 🟠 stale |  |
| [webapp-testing](https://raw.githubusercontent.com/anthropics/skills/main/skills/webapp-testing/SKILL.md) | anthropics | Claude+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 50/100 | 🟠 stale |  |
| [winmd-api-search](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/winmd-api-search/SKILL.md) | github | Copilot+Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 50/100 | 🟠 stale |  |
| [youtube-transcript](https://raw.githubusercontent.com/michalparkola/tapestry-skills-for-claude-code/main/youtube-transcript/SKILL.md) | tapestry | Universal | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 50/100 | 🟡 maintained |  |
| [add-educational-comments](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/add-educational-comments/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [agent-governance](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/agent-governance/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [agent-owasp-compliance](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/agent-owasp-compliance/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [agent-supply-chain](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/agent-supply-chain/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [agentic-eval](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/agentic-eval/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [ai-prompt-engineering-safety-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ai-prompt-engineering-safety-review/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [arch-linux-triage](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/arch-linux-triage/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [architecture-blueprint-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/architecture-blueprint-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [aspnet-minimal-api-openapi](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aspnet-minimal-api-openapi/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [atlassian](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/atlassian/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [automate-this](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/automate-this/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [autoresearch](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/autoresearch/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [aws-cdk-python-setup](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/aws-cdk-python-setup/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [az-cost-optimize](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/az-cost-optimize/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [azure-devops](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/azure-devops/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [azure-resource-health-diagnose](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-resource-health-diagnose/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [azure-role-selector](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-role-selector/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [azure-static-web-apps](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/azure-static-web-apps/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [bigquery-pipeline-audit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/bigquery-pipeline-audit/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [boost-prompt](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/boost-prompt/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [brand-guidelines](https://raw.githubusercontent.com/anthropics/skills/main/skills/brand-guidelines/SKILL.md) | anthropics | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [breakdown-epic-arch](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/breakdown-epic-arch/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [breakdown-epic-pm](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/breakdown-epic-pm/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [breakdown-feature-prd](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/breakdown-feature-prd/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [breakdown-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/breakdown-plan/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [breakdown-test](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/breakdown-test/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [canvas-design](https://raw.githubusercontent.com/anthropics/skills/main/skills/canvas-design/SKILL.md) | anthropics | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [centos-linux-triage](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/centos-linux-triage/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [chrome-devtools](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/chrome-devtools/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [code-exemplars-blueprint-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/code-exemplars-blueprint-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [code-transfer](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/code-operations-plugin/skills/code-transfer/SKILL.md) | claude-marketplace-code | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [comment-code-generate-a-tutorial](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/comment-code-generate-a-tutorial/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [containerize-aspnet-framework](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/containerize-aspnet-framework/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [containerize-aspnetcore](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/containerize-aspnetcore/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [context-map](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/context-map/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [conventional-commit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/conventional-commit/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [conversation-analyzer](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/productivity-skills-plugin/skills/conversation-analyzer/SKILL.md) | claude-marketplace-productivity | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [convert-plaintext-to-md](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/convert-plaintext-to-md/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [copilot-cli-quickstart](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/copilot-cli-quickstart/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [copilot-instructions-blueprint-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/copilot-instructions-blueprint-generator/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [copilot-spaces](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/copilot-spaces/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [copilot-usage-metrics](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/copilot-usage-metrics/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [cosmos-vulnerability-scanner](https://raw.githubusercontent.com/trailofbits/skills/main/plugins/building-secure-contracts/skills/cosmos-vulnerability-scanner/SKILL.md) | trailofbits | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ✅ | 40/100 | 🟠 stale |  |
| [cosmosdb-datamodeling](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/cosmosdb-datamodeling/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-agentsmd](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-agentsmd/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-architectural-decision-record](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-architectural-decision-record/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-github-action-workflow-specification](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-github-action-workflow-specification/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-github-issue-feature-from-specification](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-github-issue-feature-from-specification/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-github-issues-feature-from-implementation-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-github-issues-feature-from-implementation-plan/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-github-issues-for-unmet-specification-requirements](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-github-issues-for-unmet-specification-requirements/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-llms](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-llms/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-readme](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-readme/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-technical-spike](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-technical-spike/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [create-tldr-page](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/create-tldr-page/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [csharp-async](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/csharp-async/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [csharp-docs](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/csharp-docs/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [csharp-mstest](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/csharp-mstest/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [csharp-nunit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/csharp-nunit/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [csharp-tunit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/csharp-tunit/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [csharp-xunit](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/csharp-xunit/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [daily-prep](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/daily-prep/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [dataverse-python-advanced-patterns](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dataverse-python-advanced-patterns/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [dataverse-python-production-code](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dataverse-python-production-code/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [dataverse-python-quickstart](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dataverse-python-quickstart/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [dataverse-python-usecase-builder](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dataverse-python-usecase-builder/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [debian-linux-triage](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/debian-linux-triage/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [declarative-agents](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/declarative-agents/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [deep-research](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/deep-research/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [devops-rollout-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/devops-rollout-plan/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [doc-coauthoring](https://raw.githubusercontent.com/anthropics/skills/main/skills/doc-coauthoring/SKILL.md) | anthropics | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [documentation-writer](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/documentation-writer/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [dotnet-best-practices](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dotnet-best-practices/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [dotnet-design-pattern-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dotnet-design-pattern-review/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [dotnet-upgrade](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/dotnet-upgrade/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [editorconfig](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/editorconfig/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [ef-core](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ef-core/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [elevenlabs](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/elevenlabs/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [email-drafter](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/email-drafter/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [ensemble-solving](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/engineering-workflow-plugin/skills/ensemble-solving/SKILL.md) | claude-marketplace-engineering | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 40/100 | 🟠 stale |  |
| [entra-agent-user](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/entra-agent-user/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [exam-ready](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/exam-ready/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [feature-planning](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/engineering-workflow-plugin/skills/feature-planning/SKILL.md) | claude-marketplace-engineering | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 40/100 | 🟠 stale |  |
| [fedora-linux-triage](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/fedora-linux-triage/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [finalize-agent-prompt](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/finalize-agent-prompt/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [first-ask](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/first-ask/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [folder-structure-blueprint-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/folder-structure-blueprint-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [foundry-agent-sync](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/foundry-agent-sync/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [from-the-other-side-vega](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/from-the-other-side-vega/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gen-specs-as-issues](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gen-specs-as-issues/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [generate-custom-instructions-from-codebase](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/generate-custom-instructions-from-codebase/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [git-flow-branch-creator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/git-flow-branch-creator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [git-pushing](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/engineering-workflow-plugin/skills/git-pushing/SKILL.md) | claude-marketplace-engineering | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [github-copilot-starter](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/github-copilot-starter/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gmail](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/gmail/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [go-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/go-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [google-calendar](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/google-calendar/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [google-docs](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/google-docs/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [google-drive](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/google-drive/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [google-sheets](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/google-sheets/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [google-slides](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/google-slides/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [google-tts](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/google-tts/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-0-to-1-launch](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-0-to-1-launch/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-ai-gtm](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-ai-gtm/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-board-and-investor-communication](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-board-and-investor-communication/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-developer-ecosystem](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-developer-ecosystem/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-enterprise-account-planning](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-enterprise-account-planning/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-enterprise-onboarding](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-enterprise-onboarding/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-operating-cadence](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-operating-cadence/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-partnership-architecture](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-partnership-architecture/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-positioning-strategy](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-positioning-strategy/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-product-led-growth](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-product-led-growth/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [gtm-technical-product-pricing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/gtm-technical-product-pricing/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [huggingface-gradio](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-gradio/SKILL.md) | huggingface | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [huggingface-papers](https://raw.githubusercontent.com/huggingface/skills/main/skills/huggingface-papers/SKILL.md) | huggingface | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [image-manipulation-image-magick](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/image-manipulation-image-magick/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [imagen](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/imagen/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [import-infrastructure-as-code](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/import-infrastructure-as-code/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [integrate-context-matic](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/integrate-context-matic/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [internal-comms](https://raw.githubusercontent.com/anthropics/skills/main/skills/internal-comms/SKILL.md) | anthropics | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [java-springboot](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/java-springboot/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [javascript-typescript-jest](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/javascript-typescript-jest/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [kotlin-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/kotlin-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [kotlin-springboot](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/kotlin-springboot/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [manus](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/manus/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ✅ | ⬜ | 40/100 | 🟠 stale |  |
| [mcp-cli](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-cli/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mcp-copilot-studio-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-copilot-studio-server-generator/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mcp-create-adaptive-cards](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-create-adaptive-cards/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mcp-create-declarative-agent](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-create-declarative-agent/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mcp-deploy-manage-agents](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mcp-deploy-manage-agents/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [meeting-minutes](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/meeting-minutes/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [memory-merger](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/memory-merger/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mentoring-juniors](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mentoring-juniors/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [microsoft-code-reference](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/microsoft-code-reference/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [microsoft-docs](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/microsoft-docs/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mkdocs-translations](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/mkdocs-translations/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mssql](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/mssql/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [msstore-cli](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/msstore-cli/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [multi-stage-dockerfile](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/multi-stage-dockerfile/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [mysql](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/mysql/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [next-intl-add-language](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/next-intl-add-language/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [nuget-manager](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/nuget-manager/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [onboard-context-matic](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/onboard-context-matic/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [openapi-to-application-code](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/openapi-to-application-code/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [php-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/php-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [plantuml-ascii](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/plantuml-ascii/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [playwright-automation-fill-in-form](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/playwright-automation-fill-in-form/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [playwright-explore-website](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/playwright-explore-website/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [playwright-generate-test](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/playwright-generate-test/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [postgres](https://raw.githubusercontent.com/sanjay3290/ai-skills/main/skills/postgres/SKILL.md) | sanjay-ai-skills | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [postgresql-code-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/postgresql-code-review/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [postgresql-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/postgresql-optimization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [power-apps-code-app-scaffold](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/power-apps-code-app-scaffold/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [power-bi-dax-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/power-bi-dax-optimization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [power-bi-model-design-review](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/power-bi-model-design-review/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [power-bi-performance-troubleshooting](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/power-bi-performance-troubleshooting/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [power-bi-report-design-consultation](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/power-bi-report-design-consultation/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [power-platform-architect](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/power-platform-architect/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [power-platform-mcp-connector-suite](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/power-platform-mcp-connector-suite/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [prd](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/prd/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [premium-frontend-ui](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/premium-frontend-ui/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [project-workflow-analysis-blueprint-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/project-workflow-analysis-blueprint-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [pytest-coverage](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/pytest-coverage/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-clients-sdk](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-clients-sdk/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-deployment-options](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-deployment-options/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-horizontal-scaling](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/scaling-data-volume/horizontal-scaling/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-indexing-performance-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-performance-optimization/indexing-performance-optimization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-memory-usage-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-performance-optimization/memory-usage-optimization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-minimize-latency](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/minimize-latency/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-model-migration](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-model-migration/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-monitoring](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-monitoring/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-monitoring-debugging](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-monitoring/debugging/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-monitoring-setup](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-monitoring/setup/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-performance-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-performance-optimization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-scaling](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-scaling-data-volume](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/scaling-data-volume/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-scaling-qps](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/scaling-qps/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-scaling-query-volume](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/scaling-query-volume/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-search-quality](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-search-quality/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-search-quality-diagnosis](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-search-quality/diagnosis/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-search-speed-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-performance-optimization/search-speed-optimization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-search-strategies](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-search-quality/search-strategies/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-sliding-time-window](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/scaling-data-volume/sliding-time-window/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-tenant-scaling](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/scaling-data-volume/tenant-scaling/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-version-upgrade](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-version-upgrade/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [qdrant-vertical-scaling](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/qdrant-scaling/scaling-data-volume/vertical-scaling/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [quasi-coder](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/quasi-coder/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [readme-blueprint-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/readme-blueprint-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [refactor](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/refactor/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [refactor-method-complexity-reduce](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/refactor-method-complexity-reduce/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [remember](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/remember/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [remember-interactive-programming](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/remember-interactive-programming/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [repo-story-time](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/repo-story-time/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [review-and-refactor](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/review-and-refactor/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [roundup](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/roundup/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [ruff-recursive-fix](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/ruff-recursive-fix/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [rust-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/rust-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [salesforce-apex-quality](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/salesforce-apex-quality/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [salesforce-component-standards](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/salesforce-component-standards/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [salesforce-flow-design](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/salesforce-flow-design/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [scoutqa-test](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/scoutqa-test/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [shuffle-json-data](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/shuffle-json-data/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [slack-gif-creator](https://raw.githubusercontent.com/anthropics/skills/main/skills/slack-gif-creator/SKILL.md) | anthropics | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [snowflake-semanticview](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/snowflake-semanticview/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [sponsor-finder](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/sponsor-finder/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [sql-optimization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/sql-optimization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [structured-autonomy-generate](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/structured-autonomy-generate/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [structured-autonomy-implement](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/structured-autonomy-implement/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [structured-autonomy-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/structured-autonomy-plan/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [suggest-awesome-github-copilot-agents](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/suggest-awesome-github-copilot-agents/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [suggest-awesome-github-copilot-instructions](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/suggest-awesome-github-copilot-instructions/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [suggest-awesome-github-copilot-skills](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/suggest-awesome-github-copilot-skills/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [swift-mcp-server-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/swift-mcp-server-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [technology-stack-blueprint-generator](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/technology-stack-blueprint-generator/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [theme-factory](https://raw.githubusercontent.com/anthropics/skills/main/skills/theme-factory/SKILL.md) | anthropics | Claude+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [tldr-prompt](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/tldr-prompt/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [transloadit-media-processing](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/transloadit-media-processing/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [typespec-api-operations](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/typespec-api-operations/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [typespec-create-agent](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/typespec-create-agent/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [typespec-create-api-plugin](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/typespec-create-api-plugin/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [update-avm-modules-in-bicep](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/update-avm-modules-in-bicep/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [update-implementation-plan](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/update-implementation-plan/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [update-llms](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/update-llms/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [vercel-composition-patterns](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/composition-patterns/SKILL.md) | vercel | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [vercel-react-native-skills](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/react-native-skills/SKILL.md) | vercel | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [vscode-ext-commands](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/vscode-ext-commands/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [vscode-ext-localization](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/vscode-ext-localization/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [web-design-guidelines](https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md) | vercel | Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [what-context-needed](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/what-context-needed/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [winui3-migration-guide](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/winui3-migration-guide/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [workiq-copilot](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/workiq-copilot/SKILL.md) | github | Copilot | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [write-coding-standards-from-file](https://raw.githubusercontent.com/github/awesome-copilot/main/skills/write-coding-standards-from-file/SKILL.md) | github | Copilot+Universal | ⬜ | ✅ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 40/100 | 🟠 stale |  |
| [notebooklm](https://raw.githubusercontent.com/PleasePrompto/notebooklm-skill/master/SKILL.md) | notebooklm-skill | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 35/100 | ⚪ unknown |  |
| [blog-writing-guide](https://raw.githubusercontent.com/getsentry/skills/main/skills/blog-writing-guide/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [brand-guidelines](https://raw.githubusercontent.com/getsentry/skills/main/skills/brand-guidelines/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [code-auditor](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/productivity-skills-plugin/skills/code-auditor/SKILL.md) | claude-marketplace-productivity | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [code-execution](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/code-operations-plugin/skills/code-execution/SKILL.md) | claude-marketplace-code | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [code-refactor](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/code-operations-plugin/skills/code-refactor/SKILL.md) | claude-marketplace-code | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [code-review](https://raw.githubusercontent.com/getsentry/skills/main/skills/code-review/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [code-simplifier](https://raw.githubusercontent.com/getsentry/skills/main/skills/code-simplifier/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [codebase-documenter](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/productivity-skills-plugin/skills/codebase-documenter/SKILL.md) | claude-marketplace-productivity | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [coverage](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/coverage/SKILL.md) | nginity | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [doc-coauthoring](https://raw.githubusercontent.com/getsentry/skills/main/skills/doc-coauthoring/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [file-operations](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/code-operations-plugin/skills/file-operations/SKILL.md) | claude-marketplace-code | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [find-bugs](https://raw.githubusercontent.com/getsentry/skills/main/skills/find-bugs/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [fix](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/fix/SKILL.md) | nginity | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [project-bootstrapper](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/productivity-skills-plugin/skills/project-bootstrapper/SKILL.md) | claude-marketplace-productivity | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [report](https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/engineering-team/playwright-pro/skills/report/SKILL.md) | nginity | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [review-implementing](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/engineering-workflow-plugin/skills/review-implementing/SKILL.md) | claude-marketplace-engineering | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [sred-work-summary](https://raw.githubusercontent.com/getsentry/skills/main/skills/sred-work-summary/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [test-fixing](https://raw.githubusercontent.com/mhattingpete/claude-skills-marketplace/main/engineering-workflow-plugin/skills/test-fixing/SKILL.md) | claude-marketplace-engineering | Claude+Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |
| [typing-exclusion-worker](https://raw.githubusercontent.com/getsentry/skills/main/skills/typing-exclusion-worker/SKILL.md) | getsentry | Universal | ⬜ | ⬜ | ✅ | ✅ | ✅ | ⬜ | ⬜ | ⬜ | 30/100 | 🟠 stale |  |

<!-- AUTO-GENERATED SKILLS TABLE END -->

---

## Contributing

### Add your skills to the directory

1. **[Create a New Provider Issue](https://github.com/dmgrok/agent-plugins/issues/new?template=new-provider.yml)** with your repo details
2. A maintainer reviews the submission and starts automated validation:
   - ✅ SKILL.md format with YAML frontmatter
   - 🔒 Secrets scan (gitleaks)
   - 🛡️ Prompt injection check (Lakera Guard)
   - 📊 SKILL.md spec and security checks with no errors ([LGTM validation](https://github.com/dmgrok/LGTM_agent_skills))
3. Auto-PR created on pass → once merged, skills appear in the next daily aggregation

**See [issue #11](https://github.com/dmgrok/agent-plugins/issues/11) for an example submission.**

#### Maintainer review gate

Validation checks out the submitted repository, uses repository secrets and opens a pull request, so it never starts from an issue alone. Labels set by the issue form (such as `new-source`) are applied for every author and are **not** an approval.

1. Read the issue: the repository is public, the skills path is correct and the content looks legitimate.
2. Apply the `run-provider-validation` label, or run **Actions → Validate and Add New Provider → Run workflow** with the issue number. The workflow first checks that the person who applied the label or started the run has write, maintain or admin access.
3. The workflow removes the label when it finishes. To re-run after the contributor edits the issue, apply the label again.
4. Review the generated `add-provider-<id>` pull request before merging.

All issue fields are validated by [`scripts/provider_intake.py`](scripts/provider_intake.py) and every GitHub URL is rebuilt from the validated owner, repository and branch. Create the `run-provider-validation` label once under **Issues → Labels** and keep it out of issue templates.

### Contribute to an existing provider

Add skills to repositories accepting contributions:
[skillcreatorai/Ai-Agent-Skills](https://github.com/skillcreatorai/Ai-Agent-Skills) · [sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) · [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace)

### Local development

```bash
git clone https://github.com/dmgrok/agent-plugins.git
cd agent-plugins
pip install pyyaml pytest        # Test dependencies (same as CI)
python -m pytest -q              # Run the test suite
pip install -e ".[validation]"   # Optional: enhanced secret, semver and similarity checks
python scripts/aggregate.py      # Rebuild the catalog locally (network access, slow)
```

---

## Related Projects

- 🌐 [Browse Plugins](https://dmgrok.github.io/agent-plugins/) — Interactive web catalog
- 🔌 [MCP Mother Skills](https://github.com/dmgrok/mcp_mother_skills) — MCP server integration
- 🛡️ [LGTM Agent Skills](https://github.com/dmgrok/LGTM_agent_skills) — Quality validation tool
- 📖 [Agent Skills Spec](https://agentskills.io/specification) — Standard specification
- 💻 [skills.sh](https://skills.sh) — Package manager for agent skills

---

MIT License — Individual skills retain their original licenses.

**[🐛 Issues](https://github.com/dmgrok/agent-plugins/issues) · [💬 Discussions](https://github.com/dmgrok/agent-plugins/discussions) · [📊 Changelog](CHANGELOG.md)**
