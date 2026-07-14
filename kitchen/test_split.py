import unittest

from kitchen.split import split


class SplitTest(unittest.TestCase):
    def test_even(self):
        self.assertEqual(split(9.0, 3), [3.0, 3.0, 3.0])

    def test_uneven(self):
        self.assertEqual(split(10.0, 3), [3.33, 3.33, 3.33])


if __name__ == "__main__":
    unittest.main()
