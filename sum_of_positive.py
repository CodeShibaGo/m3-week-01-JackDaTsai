def positive_sum(arr):
    # Check if input is a list
    if not isinstance(arr, list):
        raise ValueError("Input should be a list.")

    # Check if list is empty
    if not arr:
        return 0

    # Check if all elements in the list are numbers
    if not all(isinstance(num, (int, float)) for num in arr):
        raise ValueError("All elements in the list should be numbers.")

    # Initialize the sum of positive numbers
    sum_positive = 0

    # Iterate over the array
    for num in arr:
        # Check if the number is positive
        if num > 0:
            # Add the positive number to the sum
            sum_positive += num

    # Return the sum of positive numbers
    return sum_positive