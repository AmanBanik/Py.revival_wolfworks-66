# __INIT__() constructor

class Employee:
    language = "Python"
    salary = 10000

    def __init__(self,name,language,salary):# can take multimple args apart self
        self.name=name
        self.language=language
        self.salary=salary# defined the args... all 3 instance attrbs set
        print('Created\nan \nobject')

        

harry=Employee('harry Rajput','Java',1200000000000)
# harry.name='harry Rajput'# what iff we dont leke do in it all time for a new attrb.
print(harry.name,',',harry.language,',',harry.salary)


