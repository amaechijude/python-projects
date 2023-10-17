set_1 = {1,2,3,4}
set_2 = {3,4,5,6}
result = list(set_1) + list(set_2)
result2 = set_1 | set_2
result3 = set_2.union(set_1)
print(set(result))
print()
print(result2)
print()
print(result3)