# test_business_metrics.py

import unittest
from business_metrics import profit_margin, roi, clv

class TestBusinessMetrics(unittest.TestCase):

    def test_profit_margin(self):
        self.assertAlmostEqual(profit_margin(1000, 400), 0.6)
        self.assertAlmostEqual(profit_margin(500, 500), 0)
        with self.assertRaises(ValueError):
            profit_margin(0, 500)

    def test_roi(self):
        self.assertAlmostEqual(roi(1500, 1000), 0.5)
        self.assertAlmostEqual(roi(1000, 1000), 0)
        with self.assertRaises(ValueError):
            roi(1500, 0)

    def test_clv(self):
        self.assertEqual(clv(100, 5, 10), 5000)
        self.assertEqual(clv(200, 3, 7), 4200)

if __name__ == '__main__':
    unittest.main()