# grading
mks=float(input('Enter your marks: '))

if mks<=100 and mks>90:
    print('Grade: Ex')
elif mks<=90 and mks>80:
    print('Grade: A')
elif mks<=80 and mks>70:
    print('Grade: B')
elif mks<=70 and mks>60:
    print('Grade: C')
elif mks<=60 and mks>50:
    print('Grade: D')
elif mks<=50:
    print('Grade: F')
else:
    print('Invalid')
print('Your grade is:',mks)