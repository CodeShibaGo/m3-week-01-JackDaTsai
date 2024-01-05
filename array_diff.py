def array_diff(a, b):
    diff = []  # Initialize an empty list to store the differences
    for i in a:  # Loop through each element in list a
        if i not in b:  # If the element is not in list b
            diff.append(i)  # Append the element to the diff list
    return diff  # Return the diff list
