# Multilevel Inheritance Example

# Level 1 - Base class
class Employee:
    def __init__(self):
        self.company = "TechCorp"
        self.name = "Default_employee"
        self.salary = 50000
    
    def show_details(self):
        print(f"Employee: {self.name} works at {self.company} with salary ${self.salary}")
    
    def work(self):
        print(f"{self.name} is working...")

# Level 2 - Inherits from Employee
class Programmer(Employee):
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.language = "Python"
        self.salary = 80000  # Override salary
    
    def code(self):
        print(f"{self.name} is coding in {self.language}")
    
    def show_skills(self):
        print(f"{self.name} knows {self.language} programming")

# Level 3 - Inherits from Programmer (which inherits from Employee)
class TeamLead(Programmer):
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.team_size = 5
        self.salary = 120000  # Override salary again
    
    def manage_team(self):
        print(f"{self.name} is managing a team of {self.team_size} developers")
    
    def conduct_meeting(self):
        print(f"{self.name} is conducting a team meeting")

# Creating objects and testing multilevel inheritance
print("=== Multilevel Inheritance Demo ===\n")

# Create a basic employee
emp = Employee()
emp.name = "John"
print("1. Basic Employee:")
emp.show_details()
emp.work()
print()

# Create a programmer (inherits from Employee)
prog = Programmer()
prog.name = "Alice"
print("2. Programmer (inherits from Employee):")
prog.show_details()  # Inherited from Employee
prog.work()          # Inherited from Employee
prog.code()          # Own method
prog.show_skills()   # Own method
print()

# Create a team lead (inherits from Programmer, which inherits from Employee)
lead = TeamLead()
lead.name = "Bob"
print("3. Team Lead (inherits from Programmer → Employee):")
lead.show_details()    # Inherited from Employee
lead.work()            # Inherited from Employee
lead.code()            # Inherited from Programmer
lead.show_skills()     # Inherited from Programmer
lead.manage_team()     # Own method
lead.conduct_meeting() # Own method
print()

print("=== Inheritance Chain ===")
print("Employee → Programmer → TeamLead")
print("Each level adds new functionality while inheriting from above!")