f=open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text3.txt')
data=f.readlines()# reads the lines in a txt file and placesthem in a <list>
print(data,type(data))# list appears
f.close()