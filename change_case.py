def change_case(input_str, case):
    if case == "upper":
        return input_str.upper()
    elif case == "lower":
        return input_str.lower()
    else:
        raise ValueError(f"Invalid case parameter: {case}. Expected 'upper' or 'lower'.")
