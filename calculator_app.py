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

# For choosing operation print
def calculator():
    while True:
        print("\nSimple Calculator App")
        print("Choose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        try:
            # Choosing Operation
            choice = int(input("Enter your choice (1/2/3/4): "))
            if choice < 1 or choice > 4:
                print("Invalid choice. Please choose a number from 1 to 4.")
                continue

            # Input of numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))