# Fibonachi series using a while loop
n = int(input("Enter no. of terms for the Fib series"))  # Number of terms
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
