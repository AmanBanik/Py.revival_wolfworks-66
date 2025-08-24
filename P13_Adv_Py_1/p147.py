try:
    with open('1.txt','r') as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open(r'C:\DevField\Python\Py.revival\P13_Adv_Py_1\file_cont2\2.txt','r') as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open('3.txt','r') as f:
        print(f.read())
except Exception as e:
    print(e)

print('Thank you')