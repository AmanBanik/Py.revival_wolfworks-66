# spam detection
L_spamkeys=['make a lot of money', 'buy now','subscribe this', 'click this']
msg=input("Enter the whole meassage:").lower()#normalizes all in lower cases
spam_found=False# default
for i in L_spamkeys:# used for loop and list with in keyword to  ease up
    if i in msg:
        spam_found=True# alters 
        break# stop on first detection
if spam_found:
    print("It's a Spam")
else:
    print("Looks Normal")