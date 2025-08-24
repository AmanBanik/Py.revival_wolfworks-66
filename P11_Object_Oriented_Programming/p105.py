# Adding distinct *Instance/Object*attributes for specific objects--
class Employee:
    lang1 = "Python"
    lang2 = "Java Script"   
    salary = 10000
Harry= Employee()
Harry.name='Harry Haresh'
print( Harry.name,Harry.lang1, Harry.lang2, Harry.salary)
Rohan=Employee()
Rohan.name='Rohan Robinson Roy'
Rohan.lang3='php'
print( Rohan.name,Rohan.lang1, Rohan.lang2,Rohan.lang3, Rohan.salary)