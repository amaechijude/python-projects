def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be positive"
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)
while True:
    try:
        x = int(input("Input an integer to compute the factorial: "))
    except ValueError:
        print("Enter an integer")
        continue
    break
print(factorial(x))