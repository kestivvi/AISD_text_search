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
        print(matches)
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


# text = "This is a test. Test are great, cause they testing things like tests should."
# pattern = "test"
# print(boyer_moore_search(text, pattern))