from pprint import pprint
def divisible_by_3_4(n):
    '''takes an int input N and
    returns set of numbers which are
    divisible by 3 and 4 between 1 and N'''
    int_param = int(n)
    #using intersection
    set1 = set(range(0,n,3))
    set2 = set(range(0,n,4))
    result = set1.intersection(set2)
    result.discard(0)
    #using for loop
    result2 = set()
    for items in range(1, int_param+1):
        if items % 3 == 0 and items % 4 == 0:
            result2.add(items)
    pprint(result2)
    print(" ")
    return result
x = input("Input an integer: ")
pprint(divisible_by_3_4(x))