class Letter:
    def __init__(self, letter: str, index: int = 0):
        self.letter = letter.upper()
        self.index = index
        self.in_word = False
        self.in_correct_place = False

    def is_in_word(self) -> bool:
        return self.in_word

    def is_in_correct_place(self) -> bool:
        return self.in_correct_place