# A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file.

Word = 'donkey'# lowered 'Donkey'

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text5.txt','r') as d:
    content = (d.read()).lower()

content_new = content.replace(Word,'#####')

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text5.txt','w') as d2:
    d2.write(content_new)# update the content