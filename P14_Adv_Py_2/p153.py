# Lambda function

squares= lambda x: x**2

sum= lambda a, b: a + b

factorial = lambda c: 1 if c == 0 else c * factorial(c-1)

print(squares(5))
print(sum(5, 10))
print(factorial(5))