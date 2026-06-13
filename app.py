import sqlite3
import os
import getpass
import hashlib
import secrets


def _require_env(name: str) -> str:
    """環境変数を取得する。未設定の場合は RuntimeError を送出する。

    Args:
        name: 環境変数名

    Returns:
        環境変数の値

    Raises:
        RuntimeError: 環境変数が未設定の場合
    """
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Required environment variable '{name}' is not set")
    return value


SECRET_KEY = _require_env("SECRET_KEY")
DB_PASSWORD = _require_env("DB_PASSWORD")


def hash_password(password: str, salt: bytes | None = None) -> tuple[str, str]:
    """パスワードをPBKDF2-HMAC-SHA256でハッシュ化する。

    Args:
        password: 平文パスワード
        salt: ソルトバイト列（省略時は自動生成）

    Returns:
        (hash_hex, salt_hex) のタプル
    """
    if salt is None:
        salt = secrets.token_bytes(32)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, iterations=260_000)
    return dk.hex(), salt.hex()


def verify_password(password: str, stored_hash: str, stored_salt: str) -> bool:
    """パスワードをハッシュと比較して検証する。

    Args:
        password: 検証する平文パスワード
        stored_hash: DBに保存されたハッシュ（hex文字列）
        stored_salt: DBに保存されたソルト（hex文字列）

    Returns:
        パスワードが一致すれば True
    """
    salt = bytes.fromhex(stored_salt)
    computed_hash, _ = hash_password(password, salt)
    return secrets.compare_digest(computed_hash, stored_hash)


def get_user(username: str) -> sqlite3.Row | None:
    """ユーザー名でユーザーレコードを取得する。

    Args:
        username: 検索するユーザー名

    Returns:
        ユーザーレコード、存在しない場合は None
    """
    with sqlite3.connect("users.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()


def read_file(filepath: str) -> str:
    """指定したファイルを安全に読み込む（パストラバーサル対策済み）。

    Args:
        filepath: 読み込むファイルパス（base_dir からの相対パス）

    Returns:
        ファイルの内容

    Raises:
        ValueError: パストラバーサルが検出された場合
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.abspath(os.path.join(base_dir, filepath))
    if not abs_path.startswith(base_dir + os.sep):
        raise ValueError("Access denied: path traversal detected")
    with open(abs_path) as f:
        return f.read()


def login(username: str, password: str) -> bool:
    """ユーザー名とパスワードで認証を行う。

    Args:
        username: ユーザー名
        password: 平文パスワード

    Returns:
        認証成功なら True、失敗なら False
    """
    user = get_user(username)
    if user and verify_password(password, user["password_hash"], user["password_salt"]):
        print("Login successful")
        return True
    print("Login failed")
    return False


if __name__ == "__main__":
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    login(username, password)
