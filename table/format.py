name = ["Amaechi", "Rome", "Jude"]
lang = ["Python", "Golang", "Javascript"]
perc = [80, 70, 60]
print("{:<15} {:<15} Percent".format("Name", "Language"))
for index in range(0, len(name)):
    print(f"{name[index]:<15} {lang[index]:<15} {perc[index]}")