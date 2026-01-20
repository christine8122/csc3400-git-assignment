# calculator.py
import math


def validate_number(value, name="number"):
    """Validate that a value is a number."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number")
    if math.isnan(value) or math.isinf(value):
        raise ValueError(f"{name} must be a finite number")

# Update all functions with validation
def add(a, b):
    """Add two numbers and return the result."""
    validate_number(a, "first number")
    validate_number(b, "second number")
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    validate_number(a, "first number")
    validate_number(b, "second number")
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    validate_number(a, "first number")
    validate_number(b, "second number")
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Raises an error if b is 0."""
    validate_number(a, "first number")
    validate_number(b, "second number")
    if b == 0:
        print("Cannot divide by zero")
    return a / b

#new added 

def power(base, exponent):
    """Raise base to the power of exponent."""
    validate_number(base, "first number")
    validate_number(exponent, "second number")
    return base ** exponent

def square_root(number):
    """Calculate the square root of a number."""
    validate_number(number, "first number")
    if number < 0:
        print("Cannot calculate square root of a negative number")
    return math.sqrt(number)