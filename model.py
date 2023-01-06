import re

class TextModel:
    def __init__(self):
        self.text = ""
        self.pattern = ""
        self.occurrences = 0

    def load_text(self, text):
        self.text = text

    def set_pattern(self, pattern):
        self.pattern = pattern

    def search(self):
        self.occurrences = len(re.findall(self.pattern, self.text))

    def get_occurrences(self):
        return self.occurrences
