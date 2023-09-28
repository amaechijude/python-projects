def print_pattern(num):
    '''Takes an integer and prints '*'
    from one to the entered integer 
    and decrease the print till one
    using while loop.
    '''
    count = 0
    while count < num:
        count += 1
        x = ("* ") * count
        print(x, count)
    while count > 0:
        count -= 1
        x = ("* ") * count
        print(x, count)
        if count == 1:
            break
    return "The End!"
param_1 = int(input("Input an integer: "))
print(print_pattern(param_1))