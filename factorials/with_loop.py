def factorials(x):
    factorial = 1
    if x == 0:
        return f"The factorial of {x} is 1"
    elif x < 0:
        return f"{x} is a negative number and factorial doesn't exist for negative numbers"
    else:
        for item in range(1, x+1):
            factorial *= item
        return f"The factorial of {x} is {factorial}"

num = int(input("Input a number to check the factorial: "))
print(factorials(num))
