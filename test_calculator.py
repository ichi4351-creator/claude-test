"""calculator.py のユニットテスト。"""

import unittest
from calculator import add, subtract, multiply, divide, power, average, to_str, to_number


class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_float(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)


class TestSubtract(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_negative_result(self):
        self.assertEqual(subtract(1, 5), -4)

    def test_zero(self):
        self.assertEqual(subtract(0, 0), 0)


class TestMultiply(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_negative(self):
        self.assertEqual(multiply(-2, 3), -6)


class TestDivide(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(divide(10, 2), 5)

    def test_float_result(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_negative(self):
        self.assertEqual(divide(-6, 2), -3)


class TestPower(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(power(2, 3), 8)

    def test_zero_exp(self):
        self.assertEqual(power(5, 0), 1)

    def test_zero_base_zero_exp(self):
        self.assertEqual(power(0, 0), 1)

    def test_negative_exp(self):
        self.assertAlmostEqual(power(2, -1), 0.5)

    def test_fraction_exp(self):
        self.assertAlmostEqual(power(4, 0.5), 2.0)


class TestAverage(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(average([1, 2, 3]), 2.0)

    def test_single(self):
        self.assertEqual(average([5]), 5.0)

    def test_floats(self):
        self.assertAlmostEqual(average([0.1, 0.2, 0.3]), 0.2, places=7)

    def test_empty(self):
        with self.assertRaises(ValueError):
            average([])

    def test_negative(self):
        self.assertEqual(average([-1, -2, -3]), -2.0)


class TestToStr(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(to_str(42), "42")

    def test_float(self):
        self.assertEqual(to_str(3.14), "3.14")

    def test_negative(self):
        self.assertEqual(to_str(-1), "-1")

    def test_zero(self):
        self.assertEqual(to_str(0), "0")


class TestToNumber(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(to_number("42"), 42)
        self.assertIsInstance(to_number("42"), int)

    def test_float(self):
        self.assertAlmostEqual(to_number("3.14"), 3.14)
        self.assertIsInstance(to_number("3.14"), float)

    def test_negative_int(self):
        self.assertEqual(to_number("-5"), -5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            to_number("")

    def test_whitespace_only(self):
        with self.assertRaises(ValueError):
            to_number("   ")

    def test_invalid(self):
        with self.assertRaises(ValueError):
            to_number("abc")

    def test_strips_whitespace(self):
        self.assertEqual(to_number("  10  "), 10)

    def test_inf_raises(self):
        with self.assertRaises(ValueError):
            to_number("inf")

    def test_nan_raises(self):
        with self.assertRaises(ValueError):
            to_number("nan")


if __name__ == "__main__":
    unittest.main()
