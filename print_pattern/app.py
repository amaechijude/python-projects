def print_pattern(num):
	'''Takes an integer and prints '*'
    from one to the entered integer 
    and decrease the print till one
	using for loop.
    '''
	for i in range(1, num+1):
		j = ("* " * i)
		print(j, i)
	for i in range(num, 0, -1):
		j = ("* " * i)
		print(j, i)
	return "The End!"

param_1 = int(input("Input an integer: "))
print(print_pattern(param_1))