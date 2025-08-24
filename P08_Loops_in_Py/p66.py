# program to get whether a number is prime or not
n = int(input("Enter a number to check if it is prime: "))

for i in range(2,n):
    if n % i == 0:
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is a prime number.")

# Program to print sum of first n natural numbers
x = int(input("Enter a number to find the sum of first n natural numbers: "))
sum = 0# empty variable to store sum
i = 1
while i <= x:
    sum += i
    i += 1
print(f"The sum of first {x} natural numbers is {sum}")

# factorial of a number using for loop
m=int(input("Enter a number to find its factorial: "))
fact = 1
for i in range(1, m + 1):
    fact *= i
print(f"The factorial of {n} is {fact}")