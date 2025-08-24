with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\this.txt') as f:
    content= f.read()

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\this_copy.txt','w') as g: # creates a new file
    g.write(content)