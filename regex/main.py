import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(txt.index("The"))
print(txt.index("Spain"))
print(f"Len txt = {len(txt)}")
print(x)
print(type(x))
if x:
  print("Ọ dị egwu")
else:
  print("No match")
