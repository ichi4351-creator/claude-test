import sqlite3
import os
import getpass
import hashlib


def get_user(username):
    with sqlite3.connect("users.db") as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()


def read_file(filepath):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    abs_path = os.path.abspath(os.path.join(base_dir, filepath))
    if not abs_path.startswith(base_dir):
        raise ValueError("Access denied: path traversal detected")
    with open(abs_path) as f:
        return f.read()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login(username, password):
    user = get_user(username)
    if user and user["password"] == hash_password(password):
        print("Login successful")
        return True
    print("Login failed")
    return False


SECRET_KEY = os.environ.get("SECRET_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

if __name__ == "__main__":
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    login(username, password)
