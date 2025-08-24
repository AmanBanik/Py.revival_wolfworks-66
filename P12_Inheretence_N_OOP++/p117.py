# Multiple Inheritence
class Employee:# Parent 1 
    company = "ITC"
    name='Default_name'
    salary=10000
    def show(self):
        print(f"nane of the Employee is {self.name} and the salary is {self. salary}" )

class Coder:# Parent 2
    language="Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language:{self.language}")


class Programner(Employee, Coder):# 
    company="ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self. language} language")


# a = Employee()
# c = Coder()
b = Programner()
# print(a.company, b. company,c.language)
print(b.company)
b.showLanguage()
b.show()
b.printLanguages()
