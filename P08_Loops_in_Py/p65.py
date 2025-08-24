# This code generates a multiplication table for a given number n from 1 to range. for loop 
n=int(input("Enter the number for the table: "))
k=int(input("Enter the range for the table: "))
for i in range(1, k+1):
    print(f"{n} x {i} = {n * i}")

# This code generates a multiplication table for a given number n from 1 to range. while loop 
m = int(input("Enter the number for the table: "))
l = int(input("Enter the range for the table: "))
i = 1
while i <= l:
    print(f"{m} x {i} = {m * i}")

# Programe to greet the user with their names starting with "S" in list l=['Harry', 'Sally', 'Rahul', 'John', 'Sophie']
l = ['Harry', 'Sally', 'Rahul', 'John', 'Sophie']
for name in l:
    if name.startswith('S'):
    # if name[0] == 'S':
        print(f"Hello {name}, welcome to the program!")