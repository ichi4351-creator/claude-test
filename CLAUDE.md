# CLAUDE.md

このプロジェクトのClaude Code設定ガイドです。

## プロジェクト概要

Claude CodeのSubAgents・Skills・Commandsの学習・実験用リポジトリ。
コードレビュー、ドキュメント生成、テスト実行、SEOブログ執筆などのワークフローを自動化する構成を収録しています。

## ディレクトリ構成

```
claude-test/
├── CLAUDE.md                        # このファイル
├── .claude/
│   ├── agents/                      # SubAgents定義
│   │   ├── code-reviewer.md         # コードレビュー専門エージェント
│   │   ├── doc-writer.md            # ドキュメント生成エージェント
│   │   ├── test-runner.md           # テスト生成・実行エージェント
│   │   └── seo-blog-writer.md       # SEOブログ執筆エージェント
│   ├── skills/                      # Skills定義
│   │   └── char-count/
│   │       └── SKILL.md             # 文字数カウントスキル
│   └── commands/                    # カスタムスラッシュコマンド
│       ├── review.md                # /review: コードレビュー実行
│       ├── test.md                  # /test: テスト生成・実行
│       └── blog.md                  # /blog: SEOブログ記事執筆
├── app.py                           # Pythonサンプル（セキュリティ修正済み）
├── calculator.py                    # 計算モジュール（docstring付き）
├── test_calculator.py               # ユニットテスト（23ケース）
└── README.md                        # 自己紹介
```

## SubAgents

| エージェント | トリガー例 | 主な機能 |
|---|---|---|
| `code-reviewer` | 「コードをレビューして」 | バグ・セキュリティ・パフォーマンス分析 |
| `doc-writer` | 「ドキュメントを書いて」 | docstring・README生成 |
| `test-runner` | 「テストを書いて」 | unittest生成・実行 |
| `seo-blog-writer` | 「ブログ記事を書いて」 | SEO最適化記事執筆 |

## Skills

| スキル | トリガー例 | 機能 |
|---|---|---|
| `char-count` | 「文字数を数えて」 | 4パターンの文字数カウント |

## Commands

| コマンド | 説明 |
|---|---|
| `/review` | 指定ファイルをcode-reviewerでレビュー |
| `/test` | 指定ファイルのテストをtest-runnerで生成・実行 |
| `/blog` | SEOブログ記事をseo-blog-writerで執筆 |

## 開発ルール

- コミットは日本語・英語どちらでも可
- プッシュ先: `https://github.com/ichi4351-creator/claude-test`（プライベート）
- Pythonのテストは `python -m unittest` で実行
- セキュリティ: パスワード・シークレットは環境変数で管理（`.env`はコミットしない）
