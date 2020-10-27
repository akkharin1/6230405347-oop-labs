def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def divide(a, b):
    if not b == 0:
        return a / b
    else:
        raise ValueError("Fail")


