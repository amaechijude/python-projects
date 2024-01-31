def sum_of_numbers(digit):
    """Sums all integers"""
    soln = 0
    param = []
    for num in digit:
        soln += int(num)
        param.append(int(num))
    return f"The sum total of {param} is = {soln}."

x = input("Input digits: ")
print(sum_of_numbers(x))