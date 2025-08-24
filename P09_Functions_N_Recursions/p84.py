# strip words in a list off a particular string
def rmv(L, word):
    S=[]
    for i in L:
        if (i != word):
            S.append(i.strip(word)) # strip strips out a word at begining or end of a string
    return S

L=eval(input('Enter the list of words in [] and seperated by , and in ": '))
word=input('Enter the word to strip: ')
print(rmv(L,word))