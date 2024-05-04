# Function for Addition
def add(num1, num2):
    return num1 + num2

# Function for Subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for Multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for Division
def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero!")
    return num1 / num2