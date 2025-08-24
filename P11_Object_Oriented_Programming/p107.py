# self parm.

# class Employee:
#     lang1 = "Python"
#     salary = 10000

#     def getInfo():
#         print(f'''The lang is: {lang1} and
#               the salary is: {salary}''')

# rohan= Employee()

# rohan.getInfo() # TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given
# #this is eqv to:
# # Employee.getInfo(rohan)<--- the parm

class Employee:
    lang1 = "Python"
    salary = 10000

    def getInfo(self):#accepting argument here sele defines the current object itself
        print(f'''The lang is: {self.lang1} and 
              the salary is: {self.salary}''')
    def greet(Khud):
        print('Goodday')

rohan= Employee()

rohan.getInfo()
rohan.greet()