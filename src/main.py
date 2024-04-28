from algorithms.simple_spell_checker import SimpleSpellChecker


def load_dictionary(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


if __name__ == "__main__":
    dictionary = load_dictionary("src/data/words.txt")

    simple_spell_checker = SimpleSpellChecker(dictionary)
    result = simple_spell_checker.is_correct("hello")

    print(result)
