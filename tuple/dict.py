list_tuple = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6)]

def convert_to_dict(param_tuple):
    dict_tuple = {}
    for index, values in enumerate(param_tuple):
        dict_tuple[values[0]] = values[1]
    return dict_tuple

print(convert_to_dict(list_tuple))