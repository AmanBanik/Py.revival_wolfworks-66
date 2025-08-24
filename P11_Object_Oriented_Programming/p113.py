class demo:
    a=4
    @staticmethod
    def greet():
        print('Hello!')

o=demo()
o.greet()
print(o.a) # prints the class attribute as there is no instance attribute specified

o.a=0  # instance attribute is set
print(o.a) #........ but this doesnot change the class attribute itself

