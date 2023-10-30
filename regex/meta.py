import re
''' Plus sign(+) matches one or more repetition.
    Question sign(?) matches zero or one repetition.
    Asterix sign(*) matches zero or more repetition.
    Curly braces {} matches exact repetition of integers inserted in it.
    Curly braces can take range as input.
'''
def text_match(param_text):
    '''takes text input and checks
    if it matches provided pattern'''
    #pattern
    regex_pattern = re.compile(r"Ab{2,3}")
    output = regex_pattern.search(param_text)
    if output == None:
        return f"Not Matched"
    else:
        return f"Matched"

print(text_match('Abbot'))
print(text_match("About"))