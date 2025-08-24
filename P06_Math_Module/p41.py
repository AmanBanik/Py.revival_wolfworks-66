# find hypotenuse of a right triangle
import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
hypotenuse = math.sqrt(a**2 + b**2)
# hypotenuse = math.hypot(a, b)  # alternative way
print(f'The length of the hypotenuse is: {hypotenuse}')