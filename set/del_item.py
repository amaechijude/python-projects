custom_set = {"name", "email", "age"}
my_set = {"name", "email", "age", "stack"}
custom_set.clear()
for items in list(my_set):
    if items == "email" or items == "age":
        my_set.discard(items)
print(custom_set)
print(my_set)