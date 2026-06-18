# Start Here

This page helps a first-time visitor understand Codex Maintainer Action in the First 3 minutes.

## What This Project Is

Codex Maintainer Action runs `codex-maintainer-kit` inside GitHub Actions. It generates maintenance artifacts for a repository and uploads them for human review.

## First 3 minutes

1. Read the [beginner guide](BEGINNER_GUIDE.md) if the project is new to you.
2. Skim [Use Cases](USE_CASES.md) to choose the workflow trigger.
3. Start with `workflow_dispatch` before using schedules or pull request comments.
4. Keep `comment-pr` disabled until you intentionally grant `pull-requests: write`.

## Choose Your Path

| You need | Trigger | Start with |
| --- | --- | --- |
| Manual trial | `workflow_dispatch` | `examples/workflow.yml` |
| Scheduled maintenance review | `schedule` | weekly artifact generation |
| Pull request visibility | `pull_request` | `comment-pr: "true"` with review permissions |
| Local hands-on inspection | local CLI | `codex-maintainer-kit` |

## Safety Note

The action reads the checked-out repository and writes artifacts. It does not auto-merge, auto-release, or grant Codex write access.
