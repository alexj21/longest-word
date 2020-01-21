# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import random
import string
import urllib.request
import json

class Game:
    def __init__(self):
        self.grid = []

        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        #if a var is a numeric zero or empty or a None object then it is considered as False
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        #https://wagon-dictionary.herokuapp.com/test
        url = "https://wagon-dictionary.herokuapp.com/"+word
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        return data['found']
