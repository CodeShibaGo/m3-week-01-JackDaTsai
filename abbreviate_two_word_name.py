def abbrev_name(name):
    # pass
    first, last = name.split()
    return f"{first[0]}.{last[0]}".upper()
