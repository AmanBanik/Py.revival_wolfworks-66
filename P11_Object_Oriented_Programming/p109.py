# __INIT__() constructor

class Employee:
    lang1 = "Python"
    salary = 10000

    def __init__(self):# dunder mtd... passes automatically when a new object is created
        print('Created an object')


    def getInfo(self):#accepting argument here sele defines the current object itself
        print(f'''The lang is: {self.lang1} and 
              the salary is: {self.salary}''')
        


rohan= Employee()

rohan.name='Rohan Rajput'
print(rohan.name,rohan.lang1,rohan.salary)

sujal=Employee()
raju=Employee()
ram=Employee()