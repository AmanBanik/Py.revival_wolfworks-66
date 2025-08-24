# Exception Hadling in Python

x= int(input("Enter a number: "))# 'aMaN'

print("You entered:", x)# Raise value error if input is not an integer
print("Thank you, This line will not execute if an exception(error in input) occurs.")


# Now with exception handling

try:
    a= int(input("Enter a number: "))  # 'aMaN'
    print("You entered:", a)
except Exception as e:
    print('type error:',e)

print("Thank you, This line will execute even if an exception occurs.")

# Example of handling specific exceptions
try:
    b = int(input("Enter a number: "))  # 'aMaN'
    print("You entered:", b)
except ValueError as ve:
    print('Value error:', ve)
except TypeError as te:    
    print('Type error:', te)
except Exception as e:
    print('Some other error:', e)
print("Thank you, This line will execute even if an exception occurs.")