def multiply_keys(param_dictionary):
    '''Multiplies the value
    of the keys '''
    output = 1
    param = []
    for key in param_dictionary:
        param.append(param_dictionary[key])
        output = output * param_dictionary[key]
    return f"The mulpiplication of {param} = {output}"

my_dictionary = {"one": 1, "two": 2, "three": 3, "four": 4}
print(multiply_keys(my_dictionary))