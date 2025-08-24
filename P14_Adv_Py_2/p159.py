a='The name of the student is {0}, his marks are {1} and phone number is {2}'
name=input('Enter your name: ')
marks=int(input('Enter your marks: '))
phno= int(input('Enter your phone number: '))

print(a.format(name,marks,phno))