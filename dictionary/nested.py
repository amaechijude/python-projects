from pprint import pprint
programming_language = [
    {
        "user_name": "Amaechi",
        "fav_lang": ["Python", "Golang", "JavaScript"],
        "skill_level": 10
    },
    {
        "user_name": "Rome",
        "fav_lang": ["Golang", "Bash", "Rust"],
        "skill_level": 9
    }
]
def add_new_user(param_list):
    '''Adds new user to the list
    packaged in a dictionary'''
    third_value = {}
    third_value["user_name"] = "Harry"
    third_value["fav_lang"] = ["JavaScript", "C++", "Perl"]
    third_value["skill_level"] = 8

    param_list.append(third_value)
    return param_list
output = add_new_user(programming_language)
pprint(output)