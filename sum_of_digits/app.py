digit = input("Input digits: ")
soln = 0
param = []
for num in digit:
    soln += int(num)
    param.append(int(num))
print(f"The sum total of {param} is = {soln}.\n\t Total = {soln}")