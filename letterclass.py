# Assignment 1: Shall We Play a Game?

## Overview
In this assignment, you will create a program called **WordyPy** using Object-Oriented Programming (OOP). The goal of **WordyPy** is to build a bot that can guess a hidden five-letter word based on feedback from the game engine. The bot will have six attempts to identify the target word, using feedback after each guess to improve its accuracy.

## Requirements

The rules of **WordyPy** are as follows:

1. **Each guess must be a five-letter English word.**
   - Only the 26 letters of the English alphabet are used, and case does not matter.
2. **The game engine generates a hidden five-letter word called the target word.**
3. **The bot must try to guess the target word within six attempts.**
4. **The bot reads from a datafile containing a list of allowable words** (one word per line) and must only make guesses from this list.
5. **After each guess, feedback is provided:**
   - The feedback indicates whether each character is in the correct position in the target word.
   - If not, the feedback specifies whether the character is present in the target word but in the wrong position.
6. **The bot must adapt based on feedback:**
   - If a letter's position is identified as correct, the bot must ensure that future guesses have that letter in the same position.
7. **Tests have been written for these requirements.** You must pass these tests to pass the assignment.

## Architecture

To play **WordyPy**, you must implement two classes:

### 1. `Letter` Class
- Represents a single English letter from a guess.
- Contains methods and attributes to describe whether the letter is in the target word, and if it is in the correct position.

```python
class Letter:
    def __init__(self, letter: str, index: int = 0):
        # Initialize letter attributes
        self.letter = letter.upper()
        self.index = index
        self.in_word = False
        self.in_correct_place = False

    def is_in_word(self) -> bool:
        # Returns True if the letter is in the word
        return self.in_word

    def is_in_correct_place(self) -> bool:
        # Returns True if the letter is in the correct place
        return self.in_correct_place
