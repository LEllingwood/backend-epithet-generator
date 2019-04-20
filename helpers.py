import json
import random


class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!

    Usage:
        data = Vocabulary.read_json("/path/to/data.json")
    """

    def read_json(path, mode='r'):
        with open(path, mode=mode) as handle:
            return json.load(handle)


class EpithetGenerator:
    """
    Selects random words from each columns of lists and generates a quantity 
    of epithets from the vocab file loaded from a path.
    """
    def select_words(self):
        data = Vocabulary.read_json("resources/data.json")
        # selects one random word from each column of the list to create epithet
        epithet = random.choice(data['Column 1']) + random.choice(data['Column 2']) + random.choice(data['Column 3'])
        return epithet

    def generate(self, num):
        # generates a quantity of epithets from a vocabulary file loaded from a path
        for _ in range(num):
            self.select_words()


print(EpithetGenerator().select_words())