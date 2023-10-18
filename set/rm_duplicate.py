from pprint import pprint
"remove duplicate from a list"
my_list = ["a","t",1,3,3,2,2,"a", "apple", "apple","base","love", "etc"]
output = set(my_list)
pprint(list(output))