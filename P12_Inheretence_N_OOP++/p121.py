# Class mtd

class alpha:
    a=1
    def show(self):
        print(f'The class attrb is: {self.a}')# i need the class attrb here self mtd takes the instance attrb as prefered
    
e=alpha()

e.a=45

e.show()# but instead i get here the instance one 



class delta:
    x=1

    @classmethod# yeh class walla defined attrb dekhiaga
    def sho(cls):# class jis par object chal raha hain
        print(f'The class attrb is: {cls.x}')

q=delta()

q.x=45

q.sho()# i get the class attrb