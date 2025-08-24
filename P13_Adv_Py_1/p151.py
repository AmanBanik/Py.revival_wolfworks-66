n=int(input('Enter number for table: '))

table=[n*i for i in range(1,11)]

print(table)

with open(r"C:\DevField\Python\Py.revival\P13_Adv_Py_1\file_cont2\table.txt","a") as t: #append mode
    t.write(f'Table of {n}: {str(table)} \n')# for newlines