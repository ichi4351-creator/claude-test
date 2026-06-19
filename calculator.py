"""四則演算・べき乗・平均値を提供するシンプルな計算モジュール。"""

from __future__ import annotations

import math


def add(a: float, b: float) -> float:
    """2つの数値を加算して返す。

    Args:
        a: 1つ目の数値
        b: 2つ目の数値

    Returns:
        a + b の結果
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """2つの数値を減算して返す。

    Args:
        a: 被減数
        b: 減数

    Returns:
        a - b の結果
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """2つの数値を乗算して返す。

    Args:
        a: 1つ目の数値
        b: 2つ目の数値

    Returns:
        a * b の結果
    """
    return a * b


def divide(a: float, b: float) -> float:
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


def power(base: float, exp: float) -> float:
    """base の exp 乗を返す。

    Args:
        base: 底
        exp: 指数

    Returns:
        base ** exp の結果
    """
    return base ** exp


def average(numbers: list[float]) -> float:
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


def to_str(value: float) -> str:
    """数値を文字列に変換して返す。

    Args:
        value: 変換する数値

    Returns:
        数値の文字列表現
    """
    return str(value)


def to_number(s: str) -> int | float:
    """文字列を数値（int または float）に変換して返す。

    整数として解釈できる場合は int を、そうでなければ float を返す。

    Args:
        s: 変換する文字列

    Returns:
        変換後の int または float

    Raises:
        ValueError: 数値に変換できない文字列の場合
    """
    s = s.strip()
    if not s:
        raise ValueError("Cannot convert empty string to number")
    try:
        return int(s)
    except ValueError:
        try:
            result = float(s)
            if not math.isfinite(result):
                raise ValueError(f"Cannot convert '{s}' to a finite number")
            return result
        except ValueError:
            raise ValueError(f"Cannot convert '{s}' to a number")
