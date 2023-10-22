def sum_list(x):
    if not isinstance(x, list):
        return -1
    elif len(x) == 1:
        return x[0]
    else:
        r = x[0] + sum_list(x[1:])
    return r

n = [1,2,3,4]
print(sum_list(n))