import copy
'''deepcopy duplicates a list that is a value
    to a key in a dictionary. Therefore updating one 
    won't affect the other.
    While copy refrences the same list. So updating 
    one would affect the other
'''
city_list = ["Enugu", "Lagos", "Abuja"]
language_list = ["Igbo", "Yorouba", "Hausa"]
name_list = ["PnMbah", "Sanwo Olu", "Wike"]

custom_dict = {
    "name": name_list,
    "city": city_list,
    "language": language_list
}

new_custom_dict = custom_dict.copy()
new_custom_dict_2 = copy.deepcopy(custom_dict)
custom_dict["city"].append("Nsukka")

print(custom_dict["city"])
print(new_custom_dict["city"])
print(new_custom_dict_2["city"])