---
name: summarize
description: 指定したファイルを読み込み、タイトル・トピック3つ・結論（1500字±10%）＋改善案を出力する。ファイルが存在しない・複数該当する場合はユーザーに確認する。使い方: /summarize [ファイルパス]
---

`summarize` スキルを使って、指定ファイルを要約・分析してください。

## 手順

1. 引数のファイルパスを確認する
   - 指定なし → 「要約するファイルのパスを教えてください」と尋ねる
   - 存在しない → Globで類似ファイルを検索して候補を提示する
   - 複数該当 → 一覧を表示してどれを要約するか確認する
2. `summarize` スキルの指示に従い出力する:
   - 📄 タイトル
   - 🔑 トピック（3つ・各3〜4文）
   - ✅ 結論（4〜5文）　← タイトル〜結論の合計を1500字±10%に調整
   - 💡 改善案（3つ）

## 使用例

```
/summarize README.md
/summarize calculator.py
/summarize .claude/agents/code-reviewer.md
/summarize *.py          # 複数該当 → 選択を促す
/summarize missing.txt   # 存在しない → 類似ファイルを提示
```
