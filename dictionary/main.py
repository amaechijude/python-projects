my_dictionary = {
        "Name": "Amaechi",
        "School": "Udemy",
        "Language": "Python",
        }
my_dictionary["Track"] = "Devops"
my_dictionary["Skill"] = "CI/CD"
print(my_dictionary)

for key in my_dictionary:
        if key == "Name":
                print("It exist in dictionary")
        print(key, my_dictionary[key])