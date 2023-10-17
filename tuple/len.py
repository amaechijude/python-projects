def order_by_lenght(param_sentence):
    '''Takes a sentence and returns the 
    words in a tuple from the lowest character 
    count to the highest'''
    string_list = param_sentence.split(" ")
    new_list = sorted(string_list, key=len)
    return tuple(new_list)
output = "hello python however we like the syntax you".title()
print(order_by_lenght(output))