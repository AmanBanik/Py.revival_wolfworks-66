class Employee:
    lang1 = "Python"
    salary = 10000

    def getInfo(self):#accepting argument here sele defines the current object itself
        print(f'''The lang is: {self.lang1} and 
              the salary is: {self.salary}''')
        
    @staticmethod# STATIC MTD
    def greet():
        print('Goodday')# itni si choti cheez ke liye pura object pass kar diya... sirf ak cheej bolta hain .... make it static

rohan= Employee()

rohan.getInfo()
rohan.greet()