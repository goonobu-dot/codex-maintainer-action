# Codex Maintainer Action

GitHub Action wrapper for [`codex-maintainer-kit`](https://github.com/goonobu-dot/codex-maintainer-kit).

It runs the CLI in GitHub Actions and generates Codex-ready maintenance artifacts for open source repositories:

- `OSS_MAINTENANCE_AUDIT.md`
- `MAINTAINER_BRIEF.md`
- `CODEX_TASKS.md`
- `codex-tasks.json`
- `CODEX_REVIEW.md`

The action also writes a GitHub Actions job summary with the audit score, review risk, and artifact paths. The intent is human-reviewed OSS maintenance. The action surfaces work, drafts task queues, and stores artifacts. It does not auto-merge, auto-release, or grant Codex write access.

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
| `kit-ref` | `v0.3.0` | Branch, tag, or commit of `codex-maintainer-kit` to install. |
| `comment-pr` | `false` | Post a short pull request comment with artifact paths and maintainer review guidance. |
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
| `codex-review` | Path to `CODEX_REVIEW.md`. |

## Pull Request Comment Mode

PR comments are disabled by default. Enable them only on pull request workflows where you want maintainers to see the generated artifact paths directly in the conversation:

```yaml
permissions:
  contents: read
  pull-requests: write

on:
  pull_request:

jobs:
  codex-maintenance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: goonobu-dot/codex-maintainer-action@v0.1.1
        with:
          comment-pr: "true"
          output-dir: codex-maintenance
```

The comment is intentionally short. It points to generated artifacts and repeats the human review rule instead of pasting full reports into the PR.

## Relationship To Codex Maintainer Kit

`codex-maintainer-kit` is the CLI. This repository is the GitHub-native runner.

Use the CLI locally when a maintainer wants to inspect a repository by hand. Use this action when a repository should regularly produce maintenance artifacts through GitHub Actions.

## Security Model

- No secrets are required.
- The action reads the checked-out repository and writes generated files to `output-dir`.
- Generated files are uploaded as workflow artifacts when `upload-artifact` is `true`.
- Pull request comments are posted only when `comment-pr` is `true` and the workflow grants `pull-requests: write`.
- A human maintainer reviews generated tasks before opening PRs or merging changes.

## Development

Run local contract tests:

```bash
python3 -m pytest -p no:cacheprovider tests -q
```

## License

MIT
