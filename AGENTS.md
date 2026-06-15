# Agent Instructions

## Scope

These instructions apply to the entire repository.

## Development

- Keep this repository as a thin GitHub Actions wrapper around `codex-maintainer-kit`.
- Do not duplicate CLI logic here.
- Prefer contract tests for `action.yml`, README usage, and examples.
- Run `python3 -m pytest -p no:cacheprovider tests -q` before claiming work is complete.
- Do not add secrets or token-based behavior.
