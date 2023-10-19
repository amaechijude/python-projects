a = {"a","b","c","d",1,2,3,4}
b = {"d","e",3}
c = {"c",4}

soln1 = (a.difference(b)).difference(c)
#0r
soln = a.difference(b, c)
soln2 = a - b - c
print(soln1)
print(soln2)
print(soln)

#symetric difference == returns a new set with unique elements from both 
output = a.symmetric_difference(b)
print(output)