def concatenate_nth(words):
    """Concatenate the nth letter from each word.

    - words: list of strings
    - For word at 1-based index n, take its nth character (also 1-based).
    - If any word is shorter than n, return the error message:
        "Invalid word list: not all words have required length"

    Returns the concatenated string.
    """
    if not isinstance(words, (list, tuple)):
        raise TypeError('words must be a list')

    result_chars = []
    for idx, word in enumerate(words, start=1):
        if not isinstance(word, str):
            return "Invalid word list: not all words have required length"
        if len(word) < idx:
            return "Invalid word list: not all words have required length"
        result_chars.append(word[idx-1])

    return ''.join(result_chars)
