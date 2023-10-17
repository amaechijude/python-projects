my_tuple = ("0","1","2","3","4","5","6","7","8","9")

def even_index(param_tuple):
    '''Takes a tuple and returns new tuple
    with only the even indexes'''
    custom_list = []
    for index, values in enumerate(param_tuple):
        if index % 2 == 0:
            custom_list.append(values)
    new_tuple = tuple(custom_list)
    return new_tuple

print(even_index(my_tuple))