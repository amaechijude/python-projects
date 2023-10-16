import copy
from pprint import pprint
'''deepcopy duplicates a list that is a value
    to a key in a dictionary. Therefore updating one 
    won't affect the other
'''
custom_dict = {
    "names": ["Amaechi", "Jude", "python"],
    "numbers": [1, 2, 3, 4]
}

new_dict = copy.deepcopy(custom_dict)
new_dict["names"].append("DevOps")
new_dict["numbers"].append(55)

pprint(custom_dict)
print("")
pprint(sorted(new_dict))