def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

x = int(input("Input the first number: "))
y = int(input("Input the second number: "))
operation = input("Choose any operation (+,-,*,/): ")

if operation == "+":
    answer = add(x,y)
elif operation == "-":
    answer = subtract(x,y)
elif operation == "*":
    answer = multiply(x,y)
elif operation == "/":
    answer = divide(x,y)

print(f"{x} {operation} {y} = {answer}")
