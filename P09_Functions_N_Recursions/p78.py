# greatest of three numbers

def greatest(a,b,c):
    if (a>b) and (a>c):
        return a
    elif (b>a) and (b>c):
        return b
    elif (c>a) and (c>b):
        return c

a=5
b=-66
c=16
print(f'greatest of {[a,b,c]} is {greatest(a,b,c)}')