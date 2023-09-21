print("Welcome to adding numbers within range function\n")
l = int(input("Input lower range: "))
u = int(input("Input upper range: "))
i = int(input("Input increment: "))
n = input("What numbers? Input Even, Odd or All: ")

def add_numbers_within_range(x,y,z):
    total = 0
    for numbers in range(x,y,z):
        total += numbers
    return total

result = add_numbers_within_range(l,u,i)
print(f"The sum of {n} numbers from {l} to {u-1} is {result}")
