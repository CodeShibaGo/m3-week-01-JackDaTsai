def find_capitals(word):
    # pass
    # List comprehension to create a new list containing only uppercase characters
    result = [char for char in word if char.isupper()]

    # Join the characters in the result list into a single string and return this string
    return ''.join(result)
