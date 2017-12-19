from functools import partial


def base_map_char(key, char, alphabet_cardinality=26):
    if not char.isalpha():
        return char
    elif char.isupper():
        offset = 65
    else:
        offset = 97

    return chr(offset + (ord(char) - offset + key) % alphabet_cardinality)


def base_caesar_shift(key, string, alphabet_cardinality=26):
    """
    [65..90]
    [ A..Z ]

    [97..122]
    [ a..z ]
    """
    map_char = partial(
        base_map_char, key, alphabet_cardinality=alphabet_cardinality)
    return "".join([map_char(c) for c in string])


caesar_shift = base_caesar_shift
