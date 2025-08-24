# This code generates a multiplication table for a given number n from 1 to 10. for loop inverted* ulta table 
n=int(input("Enter the number for the table: "))
for i in range(1, 11):
    print(f"{n} x {11-i} = {n *(11-i)}")

''' output pattern 
    1 ..10
    2 ..9
    3 ..8
    4 ..7
    5 ..6
    6 ..5
    7 ..4
    8 ..3 
    9 ..2
    10 ..1'''
