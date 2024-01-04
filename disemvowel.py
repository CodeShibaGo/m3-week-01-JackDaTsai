def disemvowel(s):
    # pass
    # List of vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    # List comprehension to create a new list containing only non-vowel characters
    result = [char for char in s if char not in vowels]

    # Join the characters in the result list into a single string and return this string
    return ''.join(result)
