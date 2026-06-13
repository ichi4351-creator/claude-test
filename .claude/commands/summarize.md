---
name: summarize
description: 指定したファイルを読み込み、タイトル・トピック3つ・結論の形式で要約する。使い方: /summarize [ファイルパス]
---

`summarize` スキルを使って、指定ファイルを要約してください。

## 手順

1. 引数のファイルパスを確認する
   - 指定あり → そのファイルを読み込む
   - 指定なし → 「要約するファイルのパスを教えてください」と尋ねる
2. `summarize` スキルの指示に従い、以下の形式で出力する:
   - 📄 タイトル
   - 🔑 トピック（3つ）
   - ✅ 結論

## 使用例

```
/summarize README.md
/summarize calculator.py
/summarize .claude/agents/code-reviewer.md
```
