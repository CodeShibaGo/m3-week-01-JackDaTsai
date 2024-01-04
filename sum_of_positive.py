def positive_sum(arr):
    # pass

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
