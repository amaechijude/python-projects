list_1 = [0, 1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10, 11]
list_3 = []

odd_elements = list_1[1::2]
even_elements = list_2[0::2]

list_3.extend(odd_elements)
list_3.extend(even_elements)

print(list_3)