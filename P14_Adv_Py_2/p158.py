# Reduce

from functools import reduce

L=[1,2,3,4,5]
def sum(a, b):
    return (a+b)

mul= lambda x,y : x*y

print(reduce(sum,L))

print(reduce(mul,L))