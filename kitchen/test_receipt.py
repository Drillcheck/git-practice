import unittest

from kitchen.receipt import lines


class ReceiptTest(unittest.TestCase):
    def test_one_line_per_dish(self):
        self.assertEqual(len(lines({"bibimbap": 1, "barley tea": 2})), 2)


if __name__ == "__main__":
    unittest.main()
