from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_action_metadata_declares_expected_inputs_and_outputs() -> None:
    action = (ROOT / "action.yml").read_text(encoding="utf-8")

    for expected in [
        "repo-path:",
        "output-dir:",
        "kit-ref:",
        "comment-pr:",
        "upload-artifact:",
        "artifact-name:",
        "maintenance-audit:",
        "maintainer-brief:",
        "codex-tasks:",
        "codex-tasks-json:",
        "codex-review:",
    ]:
        assert expected in action


def test_action_runs_codex_maintainer_kit_commands() -> None:
    action = (ROOT / "action.yml").read_text(encoding="utf-8")

    assert "pip install" in action
    assert "goonobu-dot/codex-maintainer-kit.git" in action
    assert "default: v0.3.0" in action
    assert "codex-maintainer-kit audit" in action
    assert "codex-maintainer-kit brief" in action
    assert "codex-maintainer-kit tasks" in action
    assert "codex-maintainer-kit review" in action
    assert "--format json" in action
    assert "GITHUB_STEP_SUMMARY" in action
    assert "gh pr comment" in action
    assert "github.event.pull_request.number" in action


def test_readme_documents_public_usage() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "goonobu-dot/codex-maintainer-action@v0.1.1" in readme
    assert "OSS_MAINTENANCE_AUDIT.md" in readme
    assert "MAINTAINER_BRIEF.md" in readme
    assert "CODEX_TASKS.md" in readme
    assert "CODEX_REVIEW.md" in readme
    assert "comment-pr" in readme
    assert "pull-requests: write" in readme
    assert "codex-maintainer-kit" in readme


def test_example_workflow_uses_action() -> None:
    workflow = (ROOT / "examples" / "workflow.yml").read_text(encoding="utf-8")

    assert "uses: goonobu-dot/codex-maintainer-action@v0.1.1" in workflow
    assert "output-dir:" in workflow


def test_smoke_workflow_runs_local_action() -> None:
    workflow = (ROOT / ".github" / "workflows" / "smoke.yml").read_text(encoding="utf-8")

    assert "uses: ./" in workflow
    assert "test -f codex-maintenance/OSS_MAINTENANCE_AUDIT.md" in workflow
    assert "test -f codex-maintenance/MAINTAINER_BRIEF.md" in workflow
    assert "test -f codex-maintenance/CODEX_TASKS.md" in workflow
    assert "test -f codex-maintenance/codex-tasks.json" in workflow
    assert "test -f codex-maintenance/CODEX_REVIEW.md" in workflow
