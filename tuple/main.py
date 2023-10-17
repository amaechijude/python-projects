my_tuple = (10,20,30,40)
a,b,c,d = my_tuple
print(f"a+b+c+d = {a+b+c+d}")
total = 0
for items in my_tuple:
    total += items
print(total)