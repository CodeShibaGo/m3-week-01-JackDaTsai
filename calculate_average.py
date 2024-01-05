def categorize_new_member(data):
    return_data = []
    for item in data:
        if item[0] >= 55 and item[1] > 7:
            return_data.append("Senior")
        else:
            return_data.append("Open")
    return return_data
