# Repeat program last for a list of such words to be censored.

Words = ['donkey','bad','ganda']

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text6.txt','r') as d:
    content = (d.read()).lower()

for word in Words:
    content= content.replace(word,'#'*len(word))

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text6.txt','w') as d2:
    d2.write(content)# update the content