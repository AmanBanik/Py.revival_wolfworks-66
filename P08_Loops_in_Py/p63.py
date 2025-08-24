n = int(input("Enter no. of terms for the Fib series"))  # Number of terms
a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b # Base formula for Fibonacci series
    count += 1# updates the count unlike for loop which does it automatically
