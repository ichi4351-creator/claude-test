"""calculator.py のユニットテスト。"""

import unittest
from calculator import add, subtract, multiply, divide, power, average


class TestAdd(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative(self):
        self.assertEqual(add(-1, -1), -2)

    def test_zero(self):
        self.assertEqual(add(0, 0), 0)

    def test_float(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)


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
        self.assertAlmostEqual(average([0.1, 0.2, 0.3]), 0.2, places=10)

    def test_empty(self):
        with self.assertRaises(ValueError):
            average([])

    def test_negative(self):
        self.assertEqual(average([-1, -2, -3]), -2.0)


if __name__ == "__main__":
    unittest.main()
