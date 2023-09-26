def sum_of_numbers(digit):
    """Sums all integers"""
    index = 0
    soln = 0
    param = []
    while index < len(digit):
        num = int(digit[index])
        soln += num 
        index += 1
        param.append(num)
    return f"The sum total of {param} is = {soln}.\n\t Total = {soln}"

x = input("Input digits: ")
print(sum_of_numbers(x))