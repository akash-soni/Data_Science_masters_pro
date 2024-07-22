# 

def add(a, b):
    """
    Returns the sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the quotient of a and b.
    Raises a ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
