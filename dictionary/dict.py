def generate_dict(x):
    """Takes an integer, computes the square
    and puts the output in a dictionary
    """
    my_dictionary = {}
    for num in range(1, x+1):
        my_dictionary[num] = num * num
        my_list.append(num)
    return my_dictionary

output = generate_dict(5)
print(output)