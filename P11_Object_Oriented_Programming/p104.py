# Class creation
class Employee:
    lang1 = "Python"
    lang2 = "Java Script"   # yeh raha mere FORM
    salary = 10000
# har employee ki liye infos same hain here these infos are *class* attributes
Harry= Employee()# Creating an instance of Employee ie x is an object of Employee class 
# Accessing class attributes
print( Harry.lang1, Harry.lang2, Harry.salary)
Rohan=Employee()
print( Rohan.lang1, Rohan.lang2, Rohan.salary)

# isko done ne fill kiya bangaya unka object both having now the same desg. attributes