# property decorators with getter-setter
class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f'The class attrb is {cls.a}')

    @property # turns the function into a property
    def name(self):
        return f'{self.fname} {self.lname}'
    
    @name.setter # sets the new values 
    def name(self,value):# created an instance attrb name .. from fname and lname defined within the function
        self.fname=value.split(' ')[0]
        self.lname=value.split(' ')[1]



e=Employee()

e.a=45

e.name='Aman Banik'
# Main chaha ta hoon yeh karne se meri prop directly set ho jaye
print(e.name)

e.show()