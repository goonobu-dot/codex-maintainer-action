# Codex Maintainer Action

GitHub Action wrapper for [`codex-maintainer-kit`](https://github.com/goonobu-dot/codex-maintainer-kit).

It runs the CLI in GitHub Actions and generates Codex-ready maintenance artifacts for open source repositories:

- `OSS_MAINTENANCE_AUDIT.md`
- `MAINTAINER_BRIEF.md`
- `CODEX_TASKS.md`
- `codex-tasks.json`

The intent is human-reviewed OSS maintenance. The action surfaces work, drafts task queues, and stores artifacts. It does not auto-merge, auto-release, or grant Codex write access.

## Usage

```yaml
name: Codex maintenance

on:
  workflow_dispatch:
  schedule:
    - cron: "0 9 * * 1"

jobs:
  codex-maintenance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: goonobu-dot/codex-maintainer-action@v0.1.1
        with:
          output-dir: codex-maintenance
```

## Inputs

| Input | Default | Description |
| --- | --- | --- |
| `repo-path` | `.` | Repository path to inspect. |
| `output-dir` | `codex-maintenance` | Directory where generated files are written. |
| `kit-ref` | `v0.2.0` | Branch, tag, or commit of `codex-maintainer-kit` to install. |
| `upload-artifact` | `true` | Upload generated files as an artifact. |
| `artifact-name` | `codex-maintenance` | Artifact name. |

## Outputs

| Output | Description |
| --- | --- |
| `output-dir` | Directory containing generated maintenance files. |
| `maintenance-audit` | Path to `OSS_MAINTENANCE_AUDIT.md`. |
| `maintainer-brief` | Path to `MAINTAINER_BRIEF.md`. |
| `codex-tasks` | Path to `CODEX_TASKS.md`. |
| `codex-tasks-json` | Path to `codex-tasks.json`. |

## Relationship To Codex Maintainer Kit

`codex-maintainer-kit` is the CLI. This repository is the GitHub-native runner.

Use the CLI locally when a maintainer wants to inspect a repository by hand. Use this action when a repository should regularly produce maintenance artifacts through GitHub Actions.

## Security Model

- No secrets are required.
- The action reads the checked-out repository and writes generated files to `output-dir`.
- Generated files are uploaded as workflow artifacts when `upload-artifact` is `true`.
- A human maintainer reviews generated tasks before opening PRs or merging changes.

## Development

Run local contract tests:

```bash
python3 -m pytest -p no:cacheprovider tests -q
```

## License

MIT
