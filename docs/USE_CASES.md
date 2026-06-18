# Use Cases

Use this page when you want to choose how to run Codex Maintainer Action.

## 1. Manual first run

Use `workflow_dispatch` when adding the action to a repository for the first time.

Good output: uploaded maintenance artifacts with no pull request comments and no scheduled noise.

## 2. Scheduled maintenance review

Use a weekly or monthly `schedule` when maintainers want a scheduled maintenance review without remembering to run the CLI.

Good output: fresh audit, brief, task queue, and review report stored as artifacts.

## 3. Pull request artifact generation

Use a `pull_request` workflow when maintainers want generated review context for every PR.

Good output: artifact paths in the workflow run, and optionally a short PR comment.

## 4. PR comment mode

Set `comment-pr: "true"` only when the workflow grants `pull-requests: write`.

Good output: a short comment pointing to generated artifacts instead of a long pasted report.

## 5. CLI plus action workflow

Use `codex-maintainer-kit` locally for deep inspection. Use this action for repeatable GitHub-side runs.
