x=int(input('Enter a number you want:'))

# Condition block 1# pehele is block ko dekhaga
if (x%2)==0:
    print('Divisible by 2')
else:
    print('Not divisible by 2')# first the operation goes through this block then next👇

# Conditional block 2# then ispe ayega
if (x>=18):
    print('An adult number!')
elif x in range(13,18):
    print('Teen number')
elif x in range(0,13):
    print('Kid number')
else:
    print('DNE!')

print('End of program!')#last part # then here