---
name: build
description: Analyzer→Builder→Reviewerの3段階パイプラインを順番に実行し、要件から完成品まで自動で仕上げる。使い方: /build [要件・ファイル・タスク内容]
---

以下の順でパイプラインを実行してください。各ステージの出力を次のステージに引き継ぎます。

## パイプライン

```
[Input] 要件・ファイル・タスク
    ↓
[Stage 1] analyzer エージェント
    → Analysis Report を出力
    ↓
[Stage 2] builder エージェント
    → Analysis Report を受け取り実装
    → Build Report を出力
    ↓
[Stage 3] reviewer エージェント
    → Build Report + コードを検証
    → Review Report を出力
    ↓
[完成] APPROVED なら完成を宣言 / NEEDS REVISION なら builder へ差し戻し
```

## 実行手順

1. **Analyzer 起動**: ユーザーの入力（引数）を `analyzer` エージェントに渡し、Analysis Report を生成する
2. **Builder 起動**: Analysis Report を `builder` エージェントに渡し、実装・Build Report を生成する
3. **Reviewer 起動**: Analysis Report・Build Report・実装コードを `reviewer` エージェントに渡し、Review Report を生成する
4. **判定**:
   - `APPROVED` → 「✅ パイプライン完了」と成果物を案内する
   - `NEEDS REVISION` → Builderにフィードバックを渡して修正ループ（最大2回）
   - `REJECTED` → ユーザーに報告しAnalyzerからの再実行を提案する

## 使用例

```
/build calculator.pyにべき乗と平均値の関数を追加して
/build app.pyのセキュリティ問題を修正して
/build ユーザー認証機能をapp.pyに追加して
```
