def recursion(x):
    if x == 0:
        c = "ok"
    else:
        recursion(x-1)
        print(x)
    return "End"
print(recursion(4))

def first():
    second()
    print("first")

def second():
    third()
    print("second")

def third():
    fourth()
    print("third")

def fourth():
    print("fourth")

print(first())