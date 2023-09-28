data = "amaechi @unn.edu.ng Mon 29th sept"
at_1 = data.find("@")
at_2 = data.find(" ", at_1)
result = data[at_1+1:at_2]
result_2 = data.split()
print(at_1)
print(at_2)
print(result)
print(result_2)