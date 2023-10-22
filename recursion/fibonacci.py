def fibonacci(x):
    assert x >= 0 and int(x) == x, 'Fibonacci can only compute positive integer'
    if x in[0,1]:
        return x
    else:
        return fibonacci(x-1) + (x -2)

print(fibonacci(10))
