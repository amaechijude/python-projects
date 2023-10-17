my_tuple = ("a","a","a","b","b","c","c","c","c","c","c","d","e")

def tuple_counter(param_tuple):
    '''returns the element
    with the max count'''
    max_count = 0
    current_item = param_tuple[0]
    for values in param_tuple:
        current_count = param_tuple.count(values)
        if current_count > max_count:
            max_count = current_count
            current_item = values
    return {"item": current_item, "frequency": max_count}
print(tuple_counter(my_tuple))