---
name: database-tips
description: データベース設計・クエリ最適化・インデックス戦略のベストプラクティスを提供する。SQLのN+1問題、インデックス設計、正規化、トランザクション管理について質問されたとき、またはDBパフォーマンス改善・スキーマ設計レビューを求められたときに使用する。
---

# Database Tips

データベース設計・運用における重要なポイントをガイドする。

## 1. インデックス戦略

### 基本ルール
- WHERE句・JOIN条件・ORDER BY句で使われるカラムにインデックスを作成する
- カーディナリティ（値の種類数）が高いカラムほどインデックス効果が大きい
- インデックスはSELECTを速くするがINSERT/UPDATE/DELETEを遅くするため、書き込み頻度を考慮する

### 複合インデックスの順序
```sql
-- 検索条件の選択性が高い順に並べる
CREATE INDEX idx_users ON users (status, created_at, email);
-- status（種類少）より email（ユニーク性高）を先にする方が効率的な場合も
```

### 避けるべきパターン
- 関数をかけたカラムへの検索（インデックスが効かない）
  ```sql
  -- NG: インデックス無効
  WHERE YEAR(created_at) = 2024
  -- OK: インデックス有効
  WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31'
  ```

---

## 2. N+1問題の解消

N+1問題：1回のクエリで取得したN件のレコードに対し、各レコードで追加クエリを発行してしまうパターン。

```python
# NG: N+1問題
users = db.query("SELECT * FROM users")
for user in users:
    orders = db.query(f"SELECT * FROM orders WHERE user_id = {user.id}")

# OK: JOINで1回のクエリに
users_with_orders = db.query("""
    SELECT u.*, o.*
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
""")
```

ORMを使う場合は `eager loading`（Pythonなら`joinedload`、Railsなら`includes`）を活用する。

---

## 3. トランザクション管理

```python
# 複数の更新は必ずトランザクションで囲む
with db.transaction():
    db.execute("UPDATE accounts SET balance = balance - 1000 WHERE id = 1")
    db.execute("UPDATE accounts SET balance = balance + 1000 WHERE id = 2")
# 途中でエラーが起きれば自動ロールバック
```

### 分離レベルの選択
| レベル | 用途 |
|---|---|
| READ COMMITTED | 一般的なWebアプリ（デフォルト推奨） |
| REPEATABLE READ | レポート・集計処理 |
| SERIALIZABLE | 厳密な整合性が必要な金融処理 |

---

## 4. スキーマ設計のチェックリスト

- [ ] 主キーはサロゲートキー（auto increment / UUID）を使っているか
- [ ] 外部キー制約を設定しているか
- [ ] NOT NULL制約を適切に付けているか
- [ ] 第3正規形まで正規化されているか（過度な正規化も避ける）
- [ ] `created_at` / `updated_at` カラムがあるか
- [ ] 論理削除の場合は `deleted_at` を使っているか

---

## 5. クエリ最適化の手順

1. `EXPLAIN` / `EXPLAIN ANALYZE` で実行計画を確認する
2. `Seq Scan`（全件スキャン）が出ている箇所にインデックスを検討する
3. サブクエリをJOINに書き換えられないか検討する
4. SELECT * を避け、必要なカラムのみ取得する
5. ページネーションには `OFFSET` より `keyset pagination` を使う（大量データ時）

```sql
-- NG: OFFSETは遅くなる
SELECT * FROM posts ORDER BY id LIMIT 20 OFFSET 10000;

-- OK: keyset pagination
SELECT * FROM posts WHERE id > 10000 ORDER BY id LIMIT 20;
```
