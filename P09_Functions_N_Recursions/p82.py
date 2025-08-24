def pattern(n):
    if n==0:
        return ' '
    print('*'*n)
    pattern(n-1)# same block within the block....
n=int(input('pattern length: '))
pattern(n)