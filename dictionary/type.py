from pprint import pprint

def class_type(param_list):
    '''Takes a list and returns
    the class of the items'''
    result = {}.fromkeys(param_list)
    for item in result:
        if isinstance(item, int):
            result[item] = "Integer"
        elif isinstance(item, str):
            result[item] = "String"
    return result

custom_list = [10, "one", "two", "ten", 20, 30, "five", 40]
pprint(class_type(custom_list))