---
name: performance-guide
description: コード・システムのパフォーマンス最適化ガイドを提供する。処理速度改善、メモリ効率化、キャッシュ戦略、非同期処理、プロファイリング手法について質問されたとき、またはボトルネック調査・パフォーマンスチューニングを求められたときに使用する。
---

# Performance Guide

コード・システムのパフォーマンスを改善するための手順とベストプラクティス。

## 1. パフォーマンス改善の基本手順

**計測 → 特定 → 改善 → 再計測** の順で進める。直感で最適化しない。

```python
# まずプロファイリングで本当のボトルネックを特定する
import cProfile
cProfile.run('my_function()', sort='cumulative')
```

---

## 2. Pythonのパフォーマンス改善

### ループの最適化

```python
# NG: ループ内で毎回リストに append
result = []
for i in range(10000):
    result.append(i * 2)

# OK: リスト内包表記（2〜3倍速い）
result = [i * 2 for i in range(10000)]

# OK: ジェネレータ（メモリ効率が高い）
result = (i * 2 for i in range(10000))
```

### 文字列結合

```python
# NG: ループ内で += （O(n²)）
s = ""
for word in words:
    s += word

# OK: join を使う（O(n)）
s = "".join(words)
```

### データ構造の選択

| 用途 | 推奨データ構造 | 理由 |
|---|---|---|
| 存在確認 | `set` / `dict` | O(1) ルックアップ |
| 順序付きデータ | `list` | O(1) append |
| 両端からの操作 | `collections.deque` | O(1) appendleft |
| ソート済み挿入 | `heapq` / `bisect` | O(log n) |

```python
# NG: リストで存在確認（O(n)）
if item in my_list:

# OK: setで存在確認（O(1)）
my_set = set(my_list)
if item in my_set:
```

---

## 3. キャッシュ戦略

### 関数レベルのキャッシュ

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_calculation(n):
    # 重い計算...
    return result
```

### アプリケーションレベルのキャッシュ

```python
import redis

cache = redis.Redis()

def get_user(user_id):
    cache_key = f"user:{user_id}"
    cached = cache.get(cache_key)
    if cached:
        return json.loads(cached)

    user = db.query(f"SELECT * FROM users WHERE id = ?", (user_id,))
    cache.setex(cache_key, 3600, json.dumps(user))  # 1時間キャッシュ
    return user
```

### キャッシュ設計のポイント
- TTL（有効期限）を必ず設定する
- キャッシュキーは一意になるよう設計する
- 更新時はキャッシュを削除（キャッシュ無効化）する
- メモリ使用量の上限を設定する

---

## 4. 非同期処理

### I/Oバウンドな処理（ネットワーク・ファイル）

```python
import asyncio
import aiohttp

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)  # 並列実行

# 直列: 10秒 → 並列: 1秒（10 URLの場合）
```

### CPUバウンドな処理

```python
from concurrent.futures import ProcessPoolExecutor

def cpu_heavy(data):
    # 重い計算処理
    return result

with ProcessPoolExecutor() as executor:
    results = list(executor.map(cpu_heavy, data_list))
```

---

## 5. メモリ最適化

```python
# NG: 大量データを一度にメモリに読み込む
data = open("huge_file.csv").readlines()  # 数GBのファイル

# OK: ジェネレータで逐次処理
def read_lines(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()
```

### __slots__ でメモリ削減

```python
# 通常のクラス（__dict__を持つ）
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# __slots__ でメモリを約40%削減
class Point:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## 6. パフォーマンスチェックリスト

### コードレビュー時の確認項目

- [ ] ループ内でDBクエリを発行していないか（N+1問題）
- [ ] 不要な全件取得（SELECT *）をしていないか
- [ ] 大量データをメモリに一括ロードしていないか
- [ ] 同じ計算を繰り返していないか（キャッシュで改善可能か）
- [ ] I/O処理を直列で行っていないか（並列化できるか）
- [ ] 文字列結合をループ内で行っていないか
- [ ] 存在確認にリストを使っていないか（setに変更できるか）

---

## 7. 計測ツール

```bash
# Python プロファイリング
python -m cProfile -s cumulative script.py

# メモリ計測
pip install memory-profiler
python -m memory_profiler script.py

# ベンチマーク
python -m timeit "your_code_here"
```

## レポート出力形式

パフォーマンスレビューを実施した場合は以下の形式で出力する:

```
## パフォーマンスチェック結果

### 🔴 重大なボトルネック
- [問題] (ファイル:行番号): 推定影響度

### 🟡 改善推奨
- [問題] (ファイル:行番号): 改善案

### ✅ 良好
- 非同期処理: 適切に実装されている
```
