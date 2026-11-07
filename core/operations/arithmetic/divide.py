def divide(a, b):
    a = float(a)
    b = float(b)
    if b == 0:
        raise ValueError("You cannot divide by zero.")
    return a / b