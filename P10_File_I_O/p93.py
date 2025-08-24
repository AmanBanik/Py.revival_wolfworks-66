f=open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text4.txt')
content=(f.read()).lower()

if ('twinkle' in content):
    print('The Word "Twinkle" is present in the file')
else:
    print('The Word "Twinkle" is not present in the file')

f.close()