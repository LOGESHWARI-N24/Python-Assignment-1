def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return float('inf') 
    return a / b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return float('inf')  
    return a // b

def modulus(a, b):
    if b == 0:
        return float('nan')  
    return a % b

def is_greater(a, b):
    return a > b

def is_equal(a, b):
    return a == b

def is_lesser(a, b):
    return a < b
