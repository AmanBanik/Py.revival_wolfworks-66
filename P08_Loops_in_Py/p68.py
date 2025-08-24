# This code prints a hollow diamond pattern using asterisks.
rows5 = int(input("Enter the number of rows for hollow diamond: "))
for i in range(1, rows5 + 1):
    for j in range(rows5 - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        if k == 0 or k == 2 * i - 2 or i == rows5:
            print('*', end='')# end ='' by default doesn't adds a new line
        else:
            print(' ', end='')
    print()


# create this pattern
'''
    * * ...*
    *   ...*    
    . . ...
    . . ...
    . . ... square
    *     *
    * * * *
'''
l=int(input('enter length for the square: '))
for q in range(1,l+1):
    if (q == 1) or (q == l):
        print('* '*l,)
    else:
        print('*' + '  '*(l-2) + ' *')
    print()


# This code prints a hollow rectangle pattern using asterisks.
r=int(input('length of rows /vertically: '))
c=int(input('length of column /horizontally'))

for x in range(r):
    for y in range(c):

        if (x == 0) or (x == r-1) or (y == 0) or  (y == c-1):
            print('*', end='')
        else:
            print(' ', end='')
    print()