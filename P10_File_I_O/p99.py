# Write a program to mine a log file and finde out whether it contains 'python' also specify the line number

with open(r'C:\DevField\Python\Py.revival\P10_File_I_O\file_cont1\log.txt') as f:
    lines=f.readlines()


line_no = 1

for line in lines:
    if ("Python" in line):
        print(f"'Python' is present at line: {line_no}") # at line 16
        break
    line_no += 1 # if not in the line taken, by the loop

else:
    print('"Python" is absent')