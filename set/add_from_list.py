from pprint import pprint
my_list = ["a","t",1,3,3,2,2,"a"]
output = set()
for items in my_list:
    output.add(items)
pprint(output)