import re
from text import text
def phone_no_finder(param_text):
    '''This funtion takes string param,
    checks and return a list matching nigeria
    11 digit phone number pattern'''
    a = re.findall(r"\d\d\d\d-\d\d\d-\d\d\d\d", text)
    b = re.findall(r"\d\d\d\d\d\d\d\d\d\d\d\d\d", text)
    
    if a:
        print(f"The local 11 digit {a}")
    else:
        print(f"The local digit does not exist")
    if b:
        return f"The international code is {b}"
    else:
        return r"Match does not exist"

print(phone_no_finder(text))