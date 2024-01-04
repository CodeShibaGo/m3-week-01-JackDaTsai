def unique_in_order(iterable):
    # pass
    # Initialize an empty list to store the unique elements
    unique_elements = []

    # Iterate over the iterable
    for element in iterable:
        # If the list is empty or the current element is different from the last one in the list, append it to the list
        if not unique_elements or element != unique_elements[-1]:
            unique_elements.append(element)

    # Return the list of unique elements
    return unique_elements
