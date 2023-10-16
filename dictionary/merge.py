from pprint import pprint
dict1 = {1: "one", 2: "two", 3: "three"}
dict2 = {4: "four", 5: "five", 6: "six"}

def merge_dict(param1, param2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict

pprint(merge_dict(dict1, dict2))