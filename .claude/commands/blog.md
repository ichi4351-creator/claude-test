---
name: blog
description: SEO最適化されたブログ記事をseo-blog-writerエージェントで執筆する。使い方: /blog [テーマ] [目標文字数]
---

`seo-blog-writer` エージェントを使って、SEO最適化されたブログ記事を執筆してください。

## 手順

1. 引数からテーマと目標文字数を取得する（未指定なら質問する）
2. `seo-blog-writer` エージェントに執筆を依頼する
3. `char-count` スキルで文字数を計測し、目標の ±10% に収まるよう調整する
4. 最終記事と文字数レポートを出力する

## 引数例

```
/blog Python入門 3000
/blog Claude Code SubAgents解説 5000
```
