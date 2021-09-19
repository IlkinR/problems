from problems import add
import unittest


class TestProblems(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 2), -1)
        self.assertEqual(add(0, 2), 2)


if __name__ == "__main__":
    unittest.main()
