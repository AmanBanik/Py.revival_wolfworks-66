# via loop 
f=open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text3.txt')

line=f.readline()
while (line !=''): #keeps on till the line is not blank
    print(line)
    line=f.readline()# itter the same
    
f.close()