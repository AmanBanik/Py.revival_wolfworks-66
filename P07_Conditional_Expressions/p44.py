# if elif else
a= int(input('What\'s your age:'))

if (a>=18):
    print('You are in the the age of consent(Adult)')
elif a in range(13,18):
    print('You are in teen age group')
elif a in range(13):
    print('You are a kid!')
else:
    print('You Cease to Exist!')
    print('Or, you might wish to remove the "-" sign!')