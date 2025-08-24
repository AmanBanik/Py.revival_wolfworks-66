# sum of n natural numbers
def sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    return n+sum(n-1)
n=int(input('till how many N for sum: '))
print(f'Sum of first {n} natural numbers: {sum(n)}')