# with statement
# what we normally do
f=open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text1.txt')
print(f.read())

f.close()# needed for other programes to work on the same 

# with with statement
print('\n\n\n\n\nWith WITH statement')
with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\text1.txt') as g:
    print(g.read())# all code can be written within the indent

# no need to explicitly close the file