# Raising Exceptions 
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))

if (b == 0):
    raise ZeroDivisionError('Our programe is not meant to divide a number by zero')# raising this explicitly for the condition
else:
    print('The divisionn of a/b: ', (a/b))