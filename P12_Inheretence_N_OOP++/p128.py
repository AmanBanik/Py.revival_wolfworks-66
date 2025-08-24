class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,c2):# c2 is the second complex
        return Complex(self.r + (c2.r) , self.i + (c2.i))   

    def __mul__(self, c2):
        real_part = self.r * c2.r - self. i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part,imag_part)
    
    def __str__(self): #this makes the complex object to a string
        return f'{self.r} + {self.i}i' 
    
c1=Complex(1,2)# 1+2i
c2=Complex(3,4)# 3+4i

print(c1+c2)# gives an object like <__main__.Complex object at 0x000002ABB40D5A90>

print(c1*c2)



