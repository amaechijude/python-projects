dict1 = {1: "one", 2: "two"}
dict2 = {3: "three", 4: "two"}
dict3 = {5: "five", 6: "six"}

def update_dict(param1,param2,param3):
    new_dict1 = {}
    for dicts in [param1, param2, param3]:
        new_dict1.update(dicts) 
    return new_dict1
output = update_dict(dict1,dict2,dict3)
print(output)
