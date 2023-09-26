digit = input("Input digits: ")
index = 0
soln = 0
param = []
while index < len(digit):
    num = int(digit[index])
    soln += num 
    index += 1
    param.append(num)
print(f"The sum total of {param} is = {soln}.\n\t Total = {soln}")