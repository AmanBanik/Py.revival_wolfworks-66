# program to generate multiplication tables from 2 to 20 and write it to the different files.

def gen_Tables(n):
    table=''
    for i in range(1,11):
        table += f'{n} x {i} = {n*i}\n'# we can als use f-strings this way
    
    with open(f'C:/DevField/Python/Py.revival/P10_File_I_O/file_cont1/Tables/table_{n}.txt','w') as t:
        t.write(table)# imp jab f se path likhe '/' use kare...

for x in range(2,21):
    gen_Tables(x)

# Py for automation--🤖💪