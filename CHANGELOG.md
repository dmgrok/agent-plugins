# Changelog

All notable changes to the Agent Plugins tooling, site and workflows are documented here.

Daily catalog snapshots are published as [GitHub Releases](https://github.com/dmgrok/agent-plugins/releases)
with date-based versions (`vYYYY.MM.DD`), so catalog content changes are not repeated in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Security
- The provider prompt-injection check no longer calls Lakera Guard. It scores every
  SKILL.md with pinned `protectai/deberta-v3-base-prompt-injection-v2` weights on CPU.
  A high score, a scanner error, or text the script heuristic does not treat as
  English adds `needs-review` and a summary. It does not block the provider.
  LGTM and gitleaks remain the hard gates. See `docs/prompt-injection.md`.
- Provider intake (`validate-new-provider.yml`) now starts only when a maintainer applies the
  `run-provider-validation` label or dispatches the workflow, and it verifies that person's
  repository access first. Issue-form labels such as `new-source` no longer trigger validation.
- Every issue field is validated by `scripts/provider_intake.py`, GitHub URLs are rebuilt from
  the validated owner, repository and branch, and untrusted issue content is passed through
  environment variables instead of being expanded into shell or script code.
- Workflow permissions are scoped per job, and the contributor checkout no longer persists credentials.

### Added
- Regression tests for provider intake, validation patterns and workflow hardening, run on
  every push and pull request by `.github/workflows/tests.yml`.
- Last-updated metadata for each skill.

### Fixed
- README install commands now match the site: `claude plugin marketplace add` once, then
  `claude plugin install <plugin-name>`.
- The daily catalog workflow now commits the regenerated README plugin table.
- README and docs no longer hardcode provider or plugin counts; the live badges show them.
