def count_sheep(sheep):
    # Initialize a counter variable to 0
    count = 0

    # Iterate over each element in the sheep list
    for s in sheep:
        # If the element is True, increment the count variable by 1
        if s:
            count += 1

    # Return the count variable
    return count