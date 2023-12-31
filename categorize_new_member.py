def categorize_new_member(data):
    # pass
    return_data = []
    for i in range(len(data)):
        if data[i][0] >= 55 and data[i][1] > 7:
            return_data.append("Senior")
        else:
            return_data.append("Open")
    return return_data


