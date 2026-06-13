---
name: test
description: 指定したPythonファイルのユニットテストをtest-runnerエージェントで生成・実行する。使い方: /test [ファイルパス]
---

指定されたPythonファイルのユニットテストを `test-runner` エージェントで生成し、実行してください。

## 手順

1. 引数のファイルパスを確認する（未指定なら「テスト対象ファイルを教えてください」と尋ねる）
2. `test-runner` エージェントにテスト生成を依頼する
3. `test_<filename>.py` としてテストファイルを保存する
4. `python -m unittest test_<filename> -v` で実行して結果を報告する
5. 失敗したテストがあれば原因を分析し、修正案を提示する
