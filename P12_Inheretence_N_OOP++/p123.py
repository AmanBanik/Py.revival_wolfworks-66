# Operator Overloading

class Number:
    def __init__(self, n):
        # Initialize the number
        self.n = n

    def __add__(self, num):
        # Overload + operator
        return self.n + num.n

    def __sub__(self, num):
        # Overload - operator
        return self.n - num.n

    def __mul__(self, num):
        # Overload * operator
        return self.n * num.n

    def __truediv__(self, num):
        # Overload / operator (true division)
        return self.n / num.n

    def __floordiv__(self, num):
        # Overload // operator (floor division)
        return self.n // num.n

    def __eq__(self, num):
        # Overload == operator
        return self.n == num.n

    def __lt__(self, num):
        # Overload < operator
        return self.n < num.n

    def __gt__(self, num):
        # Overload > operator
        return self.n > num.n

    def __le__(self, num):
        # Overload <= operator
        return self.n <= num.n

    def __ge__(self, num):
        # Overload >= operator
        return self.n >= num.n

    def __ne__(self, num):
        # Overload != operator
        return self.n != num.n

# Example usage
n = Number(1)
m = Number(2)

print("Addition:", n + m)
print("Subtraction:", n - m)
print("Multiplication:", n * m)
print("True Division:", n / m)
print("Floor Division:", n // m)

print("Equal:", n == m)
print("Less than:", n < m)
print("Greater than:", n > m)
print("Less than or equal:", n <= m)
print("Greater than or equal:", n >= m)
print("Not equal:", n != m)