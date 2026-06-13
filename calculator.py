"""四則演算・べき乗・平均値を提供するシンプルな計算モジュール。"""


def add(a, b):
    """2つの数値を加算して返す。

    Args:
        a: 1つ目の数値
        b: 2つ目の数値

    Returns:
        a + b の結果
    """
    return a + b


def subtract(a, b):
    """2つの数値を減算して返す。

    Args:
        a: 被減数
        b: 減数

    Returns:
        a - b の結果
    """
    return a - b


def multiply(a, b):
    """2つの数値を乗算して返す。

    Args:
        a: 1つ目の数値
        b: 2つ目の数値

    Returns:
        a * b の結果
    """
    return a * b


def divide(a, b):
    """2つの数値を除算して返す。

    Args:
        a: 被除数
        b: 除数（0以外）

    Returns:
        a / b の結果

    Raises:
        ValueError: b が 0 の場合
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exp):
    """base の exp 乗を返す。

    Args:
        base: 底
        exp: 指数

    Returns:
        base ** exp の結果
    """
    return base ** exp


def average(numbers):
    """数値リストの平均値を返す。

    Args:
        numbers: 数値のリスト（空不可）

    Returns:
        リストの平均値

    Raises:
        ValueError: numbers が空の場合
    """
    if not numbers:
        raise ValueError("List must not be empty")
    return sum(numbers) / len(numbers)
