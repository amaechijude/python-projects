name = {
    1: "one",
    2: "90"
}
namel = ["name", "language", "email"]

new_dict = {}.fromkeys(namel, "O di egwu")
new_dict["name"] = "Amaechi"
new_dict["language"] = "python"
print(3 in name, 1 in name)
print("O di egwu" in new_dict.values())
print(new_dict)
print(len(new_dict))