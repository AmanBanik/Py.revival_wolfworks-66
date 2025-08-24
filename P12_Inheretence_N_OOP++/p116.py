# Inheritence
# Single Inheritence

class Employee:# parent class
    company="ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}" )


# class Programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}" )
#     def showLanguage(self):
#         print(f"name is {self.name} and he is good with {self. language} language")

class Programmer(Employee):# Inherited Programmer from Employee ... child class
    company="ITC Infotech"
    def showLanguage(self):# with new functions
         print(f"name is {self.name} and he is good with {self. language} language")







a = Employee()
b=Programmer()
print(a.company, b. company)