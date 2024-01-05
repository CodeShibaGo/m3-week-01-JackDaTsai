def greet(name):
    if not isinstance(name, str):
        raise TypeError(f"Expected name to be a string, but got {type(name).__name__}")

    # If the name is "Johnny", return a special greeting
    if name == "Johnny":
        return "Hello, my love!"
    # Otherwise, return a regular greeting that includes the name
    else:
        return f"Hello, {name}!"
