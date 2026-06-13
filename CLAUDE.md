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
│   │   ├── char-count/
│   │   │   └── SKILL.md             # 文字数カウントスキル
│   │   ├── database-tips/
│   │   │   └── SKILL.md             # DB設計・クエリ最適化スキル
│   │   ├── security-checks/
│   │   │   └── SKILL.md             # セキュリティチェックスキル
│   │   ├── performance-guide/
│   │   │   └── SKILL.md             # パフォーマンス最適化スキル
│   │   └── summarize/
│   │       └── SKILL.md             # ファイル要約スキル
│   └── commands/                    # カスタムスラッシュコマンド
│       ├── review.md                # /review: コードレビュー実行
│       ├── test.md                  # /test: テスト生成・実行
│       ├── blog.md                  # /blog: SEOブログ記事執筆
│       └── summarize.md             # /summarize: ファイル要約
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
| `database-tips` | 「DBの設計を教えて」「N+1を直したい」 | DB設計・クエリ最適化・インデックス戦略 |
| `security-checks` | 「セキュリティチェックして」 | OWASP Top 10チェックリスト・脆弱性対策 |
| `performance-guide` | 「パフォーマンスを改善したい」 | 処理速度・メモリ・キャッシュ・非同期最適化 |
| `summarize` | 「要約して」「まとめて」 | タイトル・トピック3つ・結論の形式でファイルを要約 |

## Commands

| コマンド | 説明 |
|---|---|
| `/review` | 指定ファイルをcode-reviewerでレビュー |
| `/test` | 指定ファイルのテストをtest-runnerで生成・実行 |
| `/blog` | SEOブログ記事をseo-blog-writerで執筆 |
| `/summarize` | 指定ファイルをタイトル・トピック3つ・結論で要約 |

## 開発ルール

- コミットは日本語・英語どちらでも可
- プッシュ先: `https://github.com/ichi4351-creator/claude-test`（プライベート）
- Pythonのテストは `python -m unittest` で実行
- セキュリティ: パスワード・シークレットは環境変数で管理（`.env`はコミットしない）
