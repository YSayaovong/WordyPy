import random

class Bot:
    def __init__(self, word_list_file: str):
        # Read the list of allowable words from the file
        with open(word_list_file, 'r') as file:
            self.word_list = [line.strip().upper() for line in file.readlines()]
        self.known_letters = [None] * 5  # Store known correct letters
        self.unused_letters = set()  # Store letters not in the target word
        self.previous_guesses = set()  # Avoid repeated guesses

    def make_guess(self) -> str:
        # Filter word list based on known letters and unused letters
        possible_words = [
            word for word in self.word_list
            if all(
                (self.known_letters[i] is None or word[i] == self.known_letters[i]) and
                all(letter not in word for letter in self.unused_letters)
                for i in range(5)
            )
        ]
        # Pick a random word from the possible words
        guess = random.choice(possible_words)
        self.previous_guesses.add(guess)
        return guess

    def record_guess_results(self, guess: str, results: list):
        # Update known letters and unused letters based on feedback
        for i, letter in enumerate(results):
            if letter.is_in_correct_place():
                self.known_letters[i] = letter.letter
            elif not letter.is_in_word():
                self.unused_letters.add(letter.letter)
