# Filter

L=[7,9,5,6,4,25,7,55,44]
def even(n):
    if (n%2==0):
        return True
    return False

onlyEven= filter(even,L)
print(list(onlyEven))
