from abc import ABCMeta, abstractmethod


class ABCSimpleSpellChecker(metaclass=ABCMeta):
    @abstractmethod
    def is_correct(self, word: str) -> bool:
        pass
