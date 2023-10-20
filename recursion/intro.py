def recursion(x):
    if x == 20:
        print("Recussion")
    else:
        recursion(x+1)
        print(x)
    return "ok"

print(recursion(0))