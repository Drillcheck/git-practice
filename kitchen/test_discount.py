import unittest

from kitchen.discount import discount


class DiscountTest(unittest.TestCase):
    def test_lunch(self):
        self.assertEqual(discount(20.0, 12), 2.0)

    def test_dinner(self):
        self.assertEqual(discount(20.0, 19), 0.0)

    def test_lunch_ends(self):
        self.assertEqual(discount(20.0, 14), 0.0)


if __name__ == "__main__":
    unittest.main()
