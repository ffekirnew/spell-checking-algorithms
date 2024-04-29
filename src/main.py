from algorithms.levenshtein_distance import LevenshteinDistance
from algorithms.simple_spell_checker import SimpleSpellChecker


def load_dictionary(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    dictionary = load_dictionary("src/data/words.txt")

    simple_spell_checker = SimpleSpellChecker(dictionary)
    result = simple_spell_checker.is_correct("hello")

    levenshtein_distance = LevenshteinDistance(dictionary)
    print(LevenshteinDistance.get_distance("hello", "heivolo"))
    words = levenshtein_distance.top_k_suggestions(10, "helvo")
    for word in words:
        print(f"{word}: Distance {LevenshteinDistance.get_distance('halo', word)}")

    print(result)
