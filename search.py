def badMatchesTable(pattern):
    table = {}

    for i, c in enumerate(pattern):
        table[c] = max(1, len(table) - i - 1)
    
    return table


def boyer_moore_search(text, pattern):
    bad_table = badMatchesTable(pattern)

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
            i += bad_table[text[i]] + 1

        else:
            i += len(pattern)
    
    return matches

