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
    assert 'description: "Post a short pull request comment' in action


def test_readme_documents_public_usage() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "goonobu-dot/codex-maintainer-action@v0.2.0" in readme
    assert "OSS_MAINTENANCE_AUDIT.md" in readme
    assert "MAINTAINER_BRIEF.md" in readme
    assert "CODEX_TASKS.md" in readme
    assert "CODEX_REVIEW.md" in readme
    assert "comment-pr" in readme
    assert "pull-requests: write" in readme
    assert "Choosing `kit-ref`" in readme
    assert "kit-ref: v0.3.0" in readme
    assert "Use `main` only when testing" in readme
    assert "codex-maintainer-kit" in readme


def test_example_workflow_uses_action() -> None:
    workflow = (ROOT / "examples" / "workflow.yml").read_text(encoding="utf-8")

    assert "uses: goonobu-dot/codex-maintainer-action@v0.2.0" in workflow
    assert "output-dir:" in workflow


def test_smoke_workflow_runs_local_action() -> None:
    workflow = (ROOT / ".github" / "workflows" / "smoke.yml").read_text(encoding="utf-8")

    assert "uses: ./" in workflow
    assert "permissions:" in workflow
    assert "contents: read" in workflow
    assert "actions/checkout@v5" in workflow
    assert "test -f codex-maintenance/OSS_MAINTENANCE_AUDIT.md" in workflow
    assert "test -f codex-maintenance/MAINTAINER_BRIEF.md" in workflow
    assert "test -f codex-maintenance/CODEX_TASKS.md" in workflow
    assert "test -f codex-maintenance/codex-tasks.json" in workflow
    assert "test -f codex-maintenance/CODEX_REVIEW.md" in workflow


def test_contract_workflow_uses_minimal_permissions_and_node24_actions() -> None:
    workflow = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")

    assert "permissions:" in workflow
    assert "contents: read" in workflow
    assert "actions/checkout@v5" in workflow
    assert "actions/setup-python@v6" in workflow


def test_dependabot_covers_github_actions() -> None:
    dependabot = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")

    assert 'package-ecosystem: "github-actions"' in dependabot
    assert 'interval: "monthly"' in dependabot
    assert "version-update:semver-major" in dependabot


def test_readme_links_beginner_guides() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    assert "docs/BEGINNER_GUIDE.md" in readme
    assert "docs/BEGINNER_GUIDE.ja.md" in readme
    assert "docs/START_HERE.md" in readme
    assert "docs/START_HERE.ja.md" in readme
    assert "docs/USE_CASES.md" in readme
    assert "docs/USE_CASES.ja.md" in readme


def test_beginner_guides_explain_action_in_plain_language() -> None:
    english = (ROOT / "docs" / "BEGINNER_GUIDE.md").read_text(encoding="utf-8")
    japanese = (ROOT / "docs" / "BEGINNER_GUIDE.ja.md").read_text(encoding="utf-8")

    assert "Beginner-Friendly Guide" in english
    assert "GitHub Actions" in english
    assert "Codex Maintainer Action やさしい解説" in japanese
    assert "中学生でも分かる" in japanese


def test_start_here_and_use_cases_help_first_time_users() -> None:
    english_start = (ROOT / "docs" / "START_HERE.md").read_text(encoding="utf-8")
    japanese_start = (ROOT / "docs" / "START_HERE.ja.md").read_text(encoding="utf-8")
    english_cases = (ROOT / "docs" / "USE_CASES.md").read_text(encoding="utf-8")
    japanese_cases = (ROOT / "docs" / "USE_CASES.ja.md").read_text(encoding="utf-8")

    assert "Start Here" in english_start
    assert "First 3 minutes" in english_start
    assert "まずここから" in japanese_start
    assert "最初の3分" in japanese_start
    assert "Use Cases" in english_cases
    assert "scheduled maintenance review" in english_cases
    assert "ユースケース" in japanese_cases
    assert "定期メンテナンス確認" in japanese_cases
