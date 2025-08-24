with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\old.txt') as f:
    content = f.read()

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\renamed _by_python.txt','w') as g:
    g.write(content) # then delete old.txt manually


    # done withot os module or shutill module😒