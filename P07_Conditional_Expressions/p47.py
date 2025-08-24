# to find greatest of four numbers entered by user
'''
L=[]
a1=int(input('Enter a number'))
L.append(a1)
a2=int(input('Enter a number'))
L.append(a2)
a3=int(input('Enter a number'))
L.append(a3)
a4=int(input('Enter a number'))
L.append(a4)
print(f'Greatest of all four numbers:{max(L)}')'''
# via conditional statements
a1=int(input('Enter a number'))
a2=int(input('Enter a number'))
a3=int(input('Enter a number'))
a4=int(input('Enter a number'))

if a1>a2 and a1>a3 and a1>a4:
    print(f'{a1} is the greatest of all')
elif a2>a1 and a2>a3 and a2>a4:
    print(f'{a2} is the greatest of all')
elif a3>a1 and a3>a2 and a3>a4:
    print(f'{a3} is the greatest of all')
elif a4>a1 and a4>a2 and a4>a3:
    print(f'{a4} is the greatest of all')
else:
    print('invalid inputs')