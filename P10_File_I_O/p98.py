# Write a program to mine a log file and finde out whether it contains 'python' also specify the line number

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\log.txt') as l:
    content = l.read()

if ('Python' in content):
    print("Yes 'Python' is present in this log.txt file")

else:
    print("'Python' is absent in this log.txt file")