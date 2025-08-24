# file match check

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\this.txt') as f:
    cnt1=f.read()

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\this_copy.txt') as h:
    cnt2=h.read()

if (cnt1 == cnt2):
    print('Yes both the files are identical')

else:
    print('The files are not identical')