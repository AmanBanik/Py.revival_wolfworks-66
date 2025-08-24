import random

def game():
    print('you are playing the game')
    score=random.randint(1,62)# generates random number btw 1 and 62
    # fetch hiscore.txt
    with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\hiscore.txt') as h:
        hscore = h.read()
        if (hscore != ""):
            hscore=int(hscore)
        else:
            hscore = 0
    print(f'Your score: {score}')

    if (score > hscore):
        #write this hscore in the txt file
        with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\hiscore.txt','w') as h:
            h.write(str(score))
    return score


game()