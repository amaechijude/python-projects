digit = input("Input digits: ")
index = 0
soln = 0
#lenght = -1 * len(digit)

while index < len(digit):
    num = int(digit[index])
    soln += num 
    index += 1
    print(f"{num} {soln}")
print(f"Total is = {soln}")