# Multiplication table
def mul(n):
    for i in range(1,11):
        print(f'{n}x{i}={n*i}')

n=int(input('The number whoes table you want: '))
mul(n)