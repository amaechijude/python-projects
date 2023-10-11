from pprint import pprint
names = {
    1: "Amaechi",
    2: "Git",
    3: "Jude",
    4: "VsCode",
    5: "University"
}

def value_length(param_dictionary):
    result = {}
    for key in param_dictionary:
        lenght = len(param_dictionary[key])
        new_dictionary = {}
        new_dictionary[param_dictionary[key]] = lenght
    
        result[key] = new_dictionary
    return result

output = value_length(names)
pprint(output)