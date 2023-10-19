custom_set = {"name", "email", "age"}
my_set = {"name", "email", "age", "stack"}
# Super set
print(my_set >= custom_set)
print(my_set.issuperset(custom_set))
#Subset
print(custom_set <= my_set)
print(custom_set.issubset(my_set))