def bad_matches_table(pattern):
    return { v: max(1, len(pattern) - i - 1) for i, v in enumerate(pattern) }


def boyer_moore_search(text, pattern):
    if pattern == "":
        return []
    
    bad_table = bad_matches_table(pattern)
    matches = []
    i = len(pattern) - 1
    while i < len(text):
        j = 1
        while i < len(text) and j <= len(pattern) and text[i] == pattern[-j]:
            i -= 1
            j += 1

        if j == len(pattern) + 1:
            matches.append(i + 1)
            i += len(pattern)
        
        if text[i] in bad_table:
            i += bad_table[text[i]]
        else:
            i += len(pattern)
    
    return matches


###############################
# Sekcja testów jednostkowych
import unittest

class TestBadMatchesTable(unittest.TestCase):
    def test_bad_matches_table(self):
        self.assertDictEqual(bad_matches_table("hello"), {'h': 4, 'e': 3, 'l': 1, 'o': 1})
   
    def test_bad_matches_table_empty(self):
        self.assertDictEqual(bad_matches_table(""), {})

class TestBoyerMooreSearch(unittest.TestCase):
    def test_boyer_moore_search(self):
        self.assertEqual(boyer_moore_search("hello world", "world"), [6])
        self.assertEqual(boyer_moore_search("hello world, hello world", "world"), [6, 19])
        self.assertEqual(boyer_moore_search("abcabcabcabc", "abc"), [0, 3, 6, 9])
        self.assertEqual(boyer_moore_search("aaaaaaaaaaa", "aa"), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(boyer_moore_search("ababababababab", "ab"), [0, 2, 4, 6, 8, 10, 12])
        self.assertEqual(boyer_moore_search("abcdefghijklmnopqrstuvwxyz", "z"), [25])
   
    def test_boyer_moore_search_edge_cases(self):
        self.assertEqual(boyer_moore_search("", "a"), []) # empty text
        self.assertEqual(boyer_moore_search("abcdefg", ""), []) # empty pattern
        self.assertEqual(boyer_moore_search("abcdefg", "h"), []) # pattern not in text
        self.assertEqual(boyer_moore_search("abc def\tghi", " "), [3]) # whitespace in text
        self.assertEqual(boyer_moore_search("abcdefg", "abcdefgh"), []) # pattern longer than text

    def test_boyer_moore_search_edge_cases_2(self):
        self.assertEqual(boyer_moore_search("abcdefgabcdefg", "abcdefg"), [0, 7]) # repeated pattern
        self.assertEqual(boyer_moore_search("a"*10000, "a"*9999), [0, 1]) # large text and pattern not present
        self.assertEqual(boyer_moore_search("a"*10000, "a"*10000), [0]) # large text and pattern same
        self.assertEqual(boyer_moore_search("a"*10000, "b"), []) # different pattern and text


if __name__ == '__main__':
    unittest.main()

