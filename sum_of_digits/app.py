digit = input("Input digits: ")
soln = 0
for num in digit:
    num = int(num)
    soln += num
    print(f"{num} {soln}")
print(f"Total is = {soln}")