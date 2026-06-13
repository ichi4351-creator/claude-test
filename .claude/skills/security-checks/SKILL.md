---
name: security-checks
description: コードのセキュリティチェックリストと脆弱性対策ガイドを提供する。OWASP Top 10、認証・認可、入力検証、秘密情報管理、依存関係の脆弱性について質問されたとき、またはセキュリティレビュー・脆弱性診断を求められたときに使用する。
---

# Security Checks

コード・システムのセキュリティを確認するためのチェックリストとガイド。

## OWASP Top 10 チェックリスト

### 1. インジェクション攻撃（SQL / Command / LDAP）
```python
# NG: 文字列結合でクエリ構築
query = "SELECT * FROM users WHERE id = " + user_input

# OK: パラメータ化クエリ
cursor.execute("SELECT * FROM users WHERE id = ?", (user_input,))
```
- [ ] SQLクエリはパラメータ化クエリ / プリペアドステートメントを使用している
- [ ] シェルコマンドへの外部入力を渡していない
- [ ] ORMを使う場合でも生クエリ部分を確認している

### 2. 認証・セッション管理
- [ ] パスワードは `bcrypt` / `argon2` でハッシュ化している（MD5・SHA1は不可）
- [ ] セッショントークンは十分な長さのランダム値（32バイト以上）
- [ ] ログイン失敗回数を制限している（ブルートフォース対策）
- [ ] パスワードリセットトークンに有効期限がある

### 3. 機密データの露出
- [ ] APIキー・パスワードをソースコードに直書きしていない
- [ ] 秘密情報は環境変数 / シークレットマネージャーで管理している
- [ ] `.env`ファイルを`.gitignore`に追加している
- [ ] ログに個人情報・パスワードを出力していない

```python
# NG: ハードコード
API_KEY = "sk-abc123..."

# OK: 環境変数
import os
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise RuntimeError("API_KEY environment variable is not set")
```

### 4. XXE / パストラバーサル
```python
# パストラバーサル対策
import os

def safe_read(base_dir, user_path):
    abs_path = os.path.abspath(os.path.join(base_dir, user_path))
    if not abs_path.startswith(os.path.abspath(base_dir)):
        raise ValueError("Access denied")
    return open(abs_path).read()
```

### 5. アクセス制御
- [ ] 認証と認可を分離している（ログイン済み ≠ 権限あり）
- [ ] ユーザーIDをリクエストパラメータから取得せず、セッションから取得している
- [ ] 管理者機能へのアクセスに追加の認可チェックがある

### 6. セキュリティ設定ミス
- [ ] デバッグモードを本番環境で有効にしていない
- [ ] エラーメッセージにスタックトレース・内部情報を含めていない
- [ ] 不要なHTTPメソッド（PUT, DELETE等）を無効化している
- [ ] セキュリティヘッダーを設定している

```python
# Flaskの例: セキュリティヘッダー
@app.after_request
def set_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```

### 7. XSS（クロスサイトスクリプティング）
- [ ] ユーザー入力をHTMLに出力する際はエスケープしている
- [ ] テンプレートエンジンの自動エスケープ機能を有効にしている
- [ ] `innerHTML`の直接設定を避けている

### 8. 依存関係の脆弱性
```bash
# 脆弱性チェックコマンド
pip audit                    # Python
npm audit                    # Node.js
bundle audit                 # Ruby
```
- [ ] 定期的に依存パッケージの脆弱性チェックを実施している
- [ ] 不要なパッケージを削除している

---

## 重要度別 クイックチェック

| 重要度 | チェック項目 |
|---|---|
| 🔴 必須 | SQLインジェクション対策、パスワードハッシュ化、シークレット管理 |
| 🟠 重要 | 認証・認可の分離、入力バリデーション、エラー情報の隠蔽 |
| 🟡 推奨 | セキュリティヘッダー、依存関係の脆弱性チェック、ログの個人情報除去 |

---

## レポート出力形式

セキュリティチェックを実施した場合は以下の形式で出力する:

```
## セキュリティチェック結果

### 🔴 Critical（即時対応）
- [問題の説明] (ファイル:行番号)
  → 対応策

### 🟠 High（優先対応）
...

### ✅ 問題なし
- インジェクション対策: 問題なし
```
