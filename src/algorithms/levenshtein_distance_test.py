import unittest

from algorithms.levenshtein_distance import LevenshteinDistance


class LevenshteinDistanceTest(unittest.TestCase):
    def setUp(self):
        self.dictionary = [
            "hello",
            "world",
            "this",
            "is",
            "a",
            "simple",
            "spell",
            "checker",
        ]
        self.levenshtein_distance = LevenshteinDistance(self.dictionary)

    def test_is_correct_returns_true_for_correct_word(self):
        self.assertTrue(self.levenshtein_distance.is_correct("hello"))

    def test_is_correct_returns_false_for_incorrect_word(self):
        self.assertFalse(self.levenshtein_distance.is_correct("helo"))


if __name__ == "__main__":
    unittest.main()
