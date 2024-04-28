from abc import ABCMeta, abstractmethod
from typing import List


class ABCSuggestingSpellChecker(metaclass=ABCMeta):
    @abstractmethod
    def is_correct(self, word: str) -> bool:
        pass

    @abstractmethod
    def top_k_suggestions(self, k: int, word: str) -> List[str]:
        pass
