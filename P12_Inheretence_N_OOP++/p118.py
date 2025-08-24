# Multi level Inheritence
class alpha:
    a=1

class beta(alpha):
    b=2

class gama(beta):
    c=3

o=alpha()

print(o.a)
# print(o.b)# no b attrb in alpha

o=beta()

print(o.a,o.b)

o=gama()

print(o.a,o.b,o.c)