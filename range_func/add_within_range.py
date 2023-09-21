print("Welcome to adding numbers within range function")
l = int(input("Input lower range: "))
u = int(input("Input upper range: "))
n = input("What is the number type? Input even, odd or all: ")
def add_numbers_within_range(x,y):
    total = 0
    for numbers in range(x,y):
        if numbers % 2 == 0 and n == "even":
            total += numbers
        elif numbers % 2 == 1 and n == "odd":
            total += numbers
        elif n == "all":
            total += numbers
    return total

result = add_numbers_within_range(l,u)
print(f"The sum of {n} numbers from {l} to {u} is {result}")
