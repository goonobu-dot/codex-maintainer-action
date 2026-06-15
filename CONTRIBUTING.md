# Contributing

Thanks for helping improve Codex Maintainer Action.

## Local Checks

```bash
python3 -m pytest -p no:cacheprovider tests -q
```

## Pull Request Expectations

- Keep this repository focused on the GitHub Action wrapper.
- Do not duplicate `codex-maintainer-kit` CLI logic here.
- Update `README.md` and `examples/workflow.yml` when action inputs or behavior change.
- Include the test command and result in the pull request description.

## Human Review

AI-assisted changes are welcome, but generated changes should be reviewed by a human maintainer before merge.
