# Recursions
# factorial

def factorial(n):
    if (n == 0) or (n == 1):# this block returns 1 only as fact 0 or 1 is 1
        return 1
    return n*factorial(n-1)# for the whole def block and here the recursion happens 

n=int(input('Enter the number whoes factorial yoou want: '))

print(f'factorial of {n} is: {factorial(n)}')
    