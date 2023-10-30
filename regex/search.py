import re

txt = "The rain in Spain"
a = "The"
#Check if the string starts with "The":
x = re.search("^"+a, txt)

#Check if the string ends with "Spain"
y = re.search("Spain$", txt)

print(f"Len txt = {len(txt)}")
if x:
  print(f"Yes, txt starts with {a}")
else:
  print(f"No, txt does not starts with {a}")
if y:
  print(f"Yes, txt ends with 'Spain'")
else:
  print(f"No, txt does not end with 'Spain'")
