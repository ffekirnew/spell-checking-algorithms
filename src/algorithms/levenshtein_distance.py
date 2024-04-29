from typing import List

from algorithms.abc_suggesting_spell_checker import ABCSuggestingSpellChecker


class LevenshteinDistance(ABCSuggestingSpellChecker):
    def __init__(self, dictionary: List[str]) -> None:
        super().__init__()
        self.dictionary = dictionary

    def is_correct(self, word: str) -> bool:
        return any(
            LevenshteinDistance.get_distance(word, word_from_dictionary) == 0
            for word_from_dictionary in self.dictionary
        )

    def top_k_suggestions(self, k: int, word: str) -> List[str]:
        return sorted(
            self.dictionary,
            key=lambda word_from_dictionary: LevenshteinDistance.get_distance(
                word, word_from_dictionary
            ),
        )[:k]

    @staticmethod
    def get_distance(word1: str, word2: str) -> int:
        if len(word1) >= len(word2):
            word1, word2 = word2, word1

        if not len(word1):
            return len(word2)

        if word1[0] == word2[0]:
            return LevenshteinDistance.get_distance(word1[1:], word2[1:])

        option1 = LevenshteinDistance.get_distance(word1[1:], word2)
        option2 = LevenshteinDistance.get_distance(word1, word2[1:])
        option3 = LevenshteinDistance.get_distance(word1[1:], word2[1:])

        return 1 + min([option1, option2, option3])
