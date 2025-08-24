from functools import reduce
l = [111, 2, 65, 53, 635, 65,8]

def greater(a,b):
    if a> b:
        return a
    return b

g=reduce(greater,l)
print(g)