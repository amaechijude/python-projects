custom_set = {"name", "email", "age"}
my_set = {"name", "email", "age", "stack"}

result = custom_set.union(my_set)
output = custom_set | my_set
custom_set |= my_set
print(custom_set)
print(result)
print(output)