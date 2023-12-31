def count_duplicates(text):
    # pass
    # Dictionary to store the count of each character
    char_count = {}
    # Iterate over each character in the string
    for char in text.lower():
        # Increment the count for the character
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Count the number of characters that appear more than once
    duplicates = sum(1 for char, count in char_count.items() if count > 1)
    return duplicates
