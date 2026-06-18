# まずここから

このページは、初めて来た人が最初の3分で Codex Maintainer Action の役割をつかむための入口です。

## これは何か

Codex Maintainer Action は、`codex-maintainer-kit` を GitHub Actions 上で実行するためのアクションです。リポジトリのメンテナンス資料を作り、人間が確認できる成果物として保存します。

## 最初の3分

1. まず [やさしい解説](BEGINNER_GUIDE.ja.md) を読みます。
2. 次に [ユースケース](USE_CASES.ja.md) から、どのトリガーで使うか選びます。
3. 最初は `workflow_dispatch` で手動実行します。
4. PRコメント機能は、意図して `pull-requests: write` を付けるまで有効にしません。

## 読む順番

| やりたいこと | トリガー | 最初に見るもの |
| --- | --- | --- |
| 手動で試す | `workflow_dispatch` | `examples/workflow.yml` |
| 定期メンテナンス確認 | `schedule` | 週1回の成果物生成 |
| PR上で見える化 | `pull_request` | 権限付きの `comment-pr: "true"` |
| 手元で細かく確認 | ローカルCLI | `codex-maintainer-kit` |

## 安全面

このアクションはチェックアウトされたリポジトリを読み、成果物を書き出します。自動マージ、自動リリース、Codexへの書き込み権限付与はしません。
