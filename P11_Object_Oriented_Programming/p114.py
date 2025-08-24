from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo# must be an instance attrb. 

    def book(self,fr,to):
        print(f'Your Ticket is booked in train no.: {self.trainNo}, from {fr} to {to}')

    def getStatus(self):
        print(f'Train no.:{self.trainNo}, Running on time')

    def getFare(self,fr,to):
        print(f'Ticket fare in train no.: {self.trainNo}, from {fr} to {to} is: {randint(222,555)}')


t=Train(12399)#inst

t.book('Rampur','Saharanpur')
t.getStatus()
t.getFare('Rampur','Saharanpur')
