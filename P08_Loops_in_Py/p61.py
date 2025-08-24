#Passcalls triangle

rows1 = int(input("Enter the number of rows for pascal triangle: "))

for i in range(rows1):
    # Print leading spaces
    print(' ' * (rows1 - i), end='')

    val = 1
    for j in range(i + 1):
        print(val, end=' ')
        val = val * (i - j) // (j + 1)# floor division to avoid float values the pnc logic here
    print()


