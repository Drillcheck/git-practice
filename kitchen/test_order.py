import unittest

from kitchen.order import total, total_at


class TotalTest(unittest.TestCase):
    def test_two_dishes(self):
        self.assertEqual(total({"bibimbap": 1, "barley tea": 2}), 13.5)

    def test_lunch_total(self):
        self.assertEqual(total_at({"bibimbap": 2}, 12), 17.85)

    def test_empty_order(self):
        self.assertEqual(total({}), 0.0)


if __name__ == "__main__":
    unittest.main()
