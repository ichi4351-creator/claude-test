---
name: char-count
description: Counts characters in text and outputs 4 patterns — with/without newlines × with/without spaces. Use this skill whenever the user asks to count characters, check text length, or wants to know how many characters are in a piece of text. Trigger even if they just paste text and say "count" or "文字数". Spaces include full-width spaces (　), half-width spaces ( ), and tabs.
---

# 文字数カウント (Character Count)

ユーザーがテキストを渡したら、以下の4パターンで文字数をカウントして表形式で出力する。

## カウント対象の定義

- **スペース**: 半角スペース (U+0020)、全角スペース (U+3000)、タブ (U+0009) の3種類
- **改行**: LF (U+000A)、CR (U+000D)、CRLF すべてを改行として扱う

## 出力する4パターン

| # | 改行 | スペース |
|---|------|----------|
| 1 | 含む | 含む     |
| 2 | 含む | 含まない |
| 3 | 含まない | 含む |
| 4 | 含まない | 含まない |

## 出力フォーマット

必ずこのテーブル形式で出力する:

```
| パターン               | 文字数 |
|------------------------|--------|
| 改行あり・スペースあり | X      |
| 改行あり・スペースなし | X      |
| 改行なし・スペースあり | X      |
| 改行なし・スペースなし | X      |
```

テーブルの後に、カウント対象のテキストが何文字のテキストかを1行で自然な日本語または英語（ユーザーの言語に合わせる）で補足する。

## カウント手順

1. ユーザーのテキストをそのまま受け取る（前後のクォートや余分な整形はしない）
2. Python風の疑似コードで考えると:
   ```
   pattern1 = len(text)
   pattern2 = len(text.replace(' ', '').replace('　', '').replace('\t', ''))
   pattern3 = len(text.replace('\n', '').replace('\r', ''))
   pattern4 = len(pattern3_text.replace(' ', '').replace('　', '').replace('\t', ''))
   ```
3. 正確にカウントする（絵文字や複合文字は1文字として数える）

## 注意事項

- テキストが与えられていない場合は「カウントしたいテキストを貼り付けてください」と促す
- ユーザーが日本語で話しかけてきたら日本語で、英語なら英語で返す
- 余計な解説は不要。テーブルと補足1行だけでシンプルに返す
