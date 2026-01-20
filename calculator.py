# calculator.py
import math

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises an error if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Advanced operations
def power(base, exponent):
    """Raise base to the power of exponent."""
    return base ** exponent


def square_root(number):
    """Calculate the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(number)


def modulo(a, b):
    """Calculate remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot calculate modulo with zero")
    return a % b


def absolute_value(number):
    """Return the absolute value of a number."""
    return abs(number)