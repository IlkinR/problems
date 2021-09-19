from problems import add, contains_duplicates
import unittest


class TestProblems(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 2), -1)
        self.assertEqual(add(0, 2), 2)

    def test_contains_duplicates(self):
        self.assertEqual(contains_duplicates([1, 2, 3, 1]), True)
        self.assertEqual(contains_duplicates([1, 2, 3, 4]), False)
        self.assertEqual(contains_duplicates([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == "__main__":
    unittest.main()
