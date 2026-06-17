# Changelog

## Unreleased

- Updated CI to use minimal read permissions and Node 24-compatible GitHub Actions.
- Added Dependabot coverage for non-major GitHub Actions updates.

## 0.2.0 - 2026-06-15

- Generate `CODEX_REVIEW.md` by default using `codex-maintainer-kit` v0.3.0.
- Add GitHub Actions job summaries with audit score, review risk, artifact paths, and human review guidance.
- Add optional `comment-pr` mode for short pull request comments when workflows grant `pull-requests: write`.

## 0.1.1 - 2026-06-15

- Generate `OSS_MAINTENANCE_AUDIT.md` by default using `codex-maintainer-kit` v0.2.0.
- Add `maintenance-audit` output and smoke-test coverage.

## 0.1.0 - 2026-06-15

- Add composite GitHub Action for running `codex-maintainer-kit`.
- Generate `MAINTAINER_BRIEF.md`, `CODEX_TASKS.md`, and `codex-tasks.json`.
- Add optional artifact upload.
- Add README, example workflow, and contract tests.
