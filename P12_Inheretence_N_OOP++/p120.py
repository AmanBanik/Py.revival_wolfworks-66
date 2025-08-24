# super() mtd

class alpha:
    def __init__(self):
        print('Constructor of alpha')
    a=1

class beta(alpha):
    def __init__(self):
        print('Constructor of beta')
    b=2

class gama(beta):
    def __init__(self):
        super().__init__()# jab gama chale butv also uska parent bhi chale
        print('Constructor of gama')
    c=3

# o=alpha()

# print(o.a)

 
# o=beta()

# print(o.a,o.b)

o=gama()

print(o.a,o.b,o.c)