import search

class TextModel:
    def __init__(self):
        self.__text = ""
        self.__pattern = ""
        self.__occurrences = 0

    def set_text(self, text):
        self.__text = text
    
    def get_text(self):
        return self.__text

    def set_pattern(self, pattern):
        self.__pattern = pattern

    def get_pattern(self):
        return self.__pattern

    def search(self):
        self.__occurrences = search.boyer_moore_search(self.text, self.pattern)

    def get_occurences(self):
        return self.__occurrences
