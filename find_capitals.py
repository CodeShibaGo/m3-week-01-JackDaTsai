def find_capitals(word):
    # Initialize an empty list to store uppercase characters
    result = []

    # Iterate over each character in the input string
    for char in word:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Append the uppercase character to the result list
            result.append(char)

    # Join the characters in the result list into a single string
    joined_result = ''.join(result)

    # Return the joined string
    return joined_result
