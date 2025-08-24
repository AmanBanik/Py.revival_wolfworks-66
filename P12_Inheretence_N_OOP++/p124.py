# operator overloading

class Number:
    def __init__(self, n):
        # Initialize the number
        self.n = n

    def __str__(self):
        # User-friendly string representation
        return f"Number: {self.n}"

    def __repr__(self):
        # Developer-friendly representation
        return f"Number({self.n})"

    def __len__(self):
        # Length of the number (number of digits)
        return len(str(abs(self.n)))  # abs handles negative numbers

# Example usage
x = Number(1234)
y = Number(-56)

print(str(x))       # Output: Number: 1234
print(repr(y))      # Output: Number(-56)
print(len(x))       # Output: 4
print(len(y))       # Output: 2