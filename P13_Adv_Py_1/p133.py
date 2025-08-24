# Types definition

x : int =5 # native methoda use karne ke kam ata hain
print(x.is_integer)

y : str='Aman'

print(y)


def sum(a : int,b : int) -> int: # specify karrahe hain a and b bhi integer also the sum is an integer
    return (a+b)

print(sum(9,11))