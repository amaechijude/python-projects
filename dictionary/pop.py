names = {
        1: "Amaechi",
        2: "Jude",
        3: "git"
        }

for keys, values in list(names.items()):
    if values == "git":
        names.pop(keys)
print(names)
