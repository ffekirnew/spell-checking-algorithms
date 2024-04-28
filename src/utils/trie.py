from typing import List


class TrieNode:
    def __init__(self, is_end_of_word: bool = False):
        self.children = {}
        self.is_end_of_word = is_end_of_word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for index, char in enumerate(word):
            char_is_end_of_word = index == len(word) - 1

            if char not in curr.children:
                curr.children[char] = TrieNode(char_is_end_of_word)
            else:
                curr.children[char].is_end_of_word |= char_is_end_of_word

            curr = curr.children[char]

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False

            curr = curr.children[char]

        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

    @classmethod
    def build_trie(cls, words: List[str]) -> "Trie":
        trie = cls()

        for word in words:
            trie.insert(word)

        return trie
