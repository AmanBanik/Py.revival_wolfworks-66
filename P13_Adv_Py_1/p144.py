# Global key
a=89# global
def fub():
    global a # changes the global variable as the local one
    a=4
    print(a)# local

fub()
print(a)