# Walrus operator
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.

if (n := len("Hello, World!, Humpty Dumpty, Chale Kashmir")) > 10:
    print(f"The length of the string is {n}, which is greater than 10.")



if (x := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ( {x} elements, expected <= 3)" )
