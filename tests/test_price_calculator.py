import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from price_calculator.calc import calculate_total

class TestPriceCalculator(unittest.TestCase):
    def test_basic(self):
        costs = {'apple': 1.00, 'banana': 0.50, 'cookie': 2.25}
        items = ['apple', 'banana', 'cookie']
        self.assertEqual(calculate_total(costs, items, 10), 4.13)

    def test_missing_item(self):
        costs = {'apple': 1.00}
        items = ['apple', 'pear']
        self.assertEqual(calculate_total(costs, items, 5), 1.05)

    def test_empty_items(self):
        costs = {'apple': 1.00}
        items = []
        self.assertEqual(calculate_total(costs, items, 10), 0.00)

    def test_zero_tax(self):
        costs = {'x': 2.333}
        items = ['x']
        self.assertEqual(calculate_total(costs, items, 0), 2.33)

    def test_invalid_values(self):
        costs = {'x': 'bad', 'y': 1.25}
        items = ['x', 'y']
        self.assertEqual(calculate_total(costs, items, 10), 1.38)

if __name__ == '__main__':
    unittest.main()
