class Programmer:
    company = "Microsoft"
    def __init__(self, name,salary,language, pin):
        self.name = name
        self.salary = salary
        self.language = language
        self.pin = pin

j=Programmer("John", 50000, "JAVA", 1234)

print(j.name, j.salary, j.language, j.pin, j.company)
        

r=Programmer("Rohan", 82000, "PYTHON", 7985)

print(r.name, r.salary, r.language, r.pin, r.company)