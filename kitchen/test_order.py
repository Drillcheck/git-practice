import unittest

from kitchen.order import total


class TotalTest(unittest.TestCase):
    def test_two_dishes(self):
        self.assertEqual(total({"bibimbap": 1, "barley tea": 2}), 14.85)


if __name__ == "__main__":
    unittest.main()
