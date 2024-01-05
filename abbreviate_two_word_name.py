def abbrev_name(name):
    words = name.split()
    if len(words) != 2:
        raise ValueError("Input string should contain exactly two words")
    first, last = words
    return f"{first[0]}.{last[0]}".upper()
