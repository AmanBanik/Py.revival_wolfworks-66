# Testing out if we change self parm's slf with any thing else

from random import randint
class Train:
    def __init__(slf,trainNo):# self-->slf
        slf.trainNo=trainNo# must be an instance attrb. 

    def book(solf,fr,to):# self-->solf
        print(f'Your Ticket is booked in train no.: {solf.trainNo}, from {fr} to {to}')

    def getStatus(khud):# self--> khud
        print(f'Train no.:{khud.trainNo}, Running on time')

    def getFare(OwO,fr,to):# self--> OwO
        print(f'Ticket fare in train no.: {OwO.trainNo}, from {fr} to {to} is: {randint(222,555)}')


t=Train(12399)#inst

t.book('Rampur','Saharanpur')
t.getStatus()
t.getFare('Rampur','Saharanpur')


# Absolute---ly nothing just use proper replacements also within the functions individual methods😎