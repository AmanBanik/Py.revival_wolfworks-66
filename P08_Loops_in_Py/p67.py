# This code prints a right-angled triangle pattern using asterisks.
rows1 = int(input("Enter the number of rows: "))
for i in range(1, rows1 + 1):
    print('*' * i)

# This code prints a right-angled triangle pattern using asterisks-inverted
rows2 = int(input("Enter the number of rows for inverted triangle: "))
for i in range(1, rows2 + 1):
    print(' ' * (rows2 - i) + '*' * i)

# This code prints a right-angled triangle pattern using asterisks-inverted-inverted
rows3 = int(input("Enter the number of rows for inverted inverted triangle: "))
for i in range(rows3, 0, -1):
    print(' ' * (rows3 - i) + '*' * i)

# This code prints a diamond pattern using asterisks.
rows4 = int(input("Enter the number of rows(half way) for diamond: "))
# Upper triangle
for i in range(1, rows4 + 1):
    print(' ' * (rows4 - i) + '*' * (2 * i - 1))

# Lower inverted triangle
for i in range(rows4 - 1, 0, -1):# The logic for the lower inverted triangle step backs one row
    print(' ' * (rows4 - i) + '*' * (2 * i - 1))
