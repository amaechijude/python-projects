custom_string = 'X-MAPDS-Confidence:0.8475'
#Write a programm that returns the strings after : and converts it to float
param_1 = custom_string.find(":")
param_2 = custom_string[param_1 + 1:]
result = float(param_2)
print(round(result, 2))