class Calculator:
    def __init__(self,n):
        self.n=n
    def square(self):
        print(f'The number squared is: {self.n*self.n}')
    def cube(self):
        print(f'The number cubed is: {self.n*self.n*self.n}')
    def sqroot(self):
        print(f'Square root of the number is: {self.n**0.5}')

a=Calculator(5)

a.square()
a.cube()
a.sqroot()