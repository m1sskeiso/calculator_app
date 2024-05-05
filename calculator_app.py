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

            # Operations 
            if choice == 1:
                result = add(num1, num2)
                operation = "Addition"
            elif choice == 2:
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == 3:
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == 4:
                result = divide(num1, num2)
                operation = "Division"

            print(f"\nResult of {operation}: {num1} {operation} {num2} = {result}")
        
        except ValueError as ve:
            print("Error:", ve)
            print("Please enter valid numbers.")
            continue

        except Exception as e:
            print("An error occurred:", e)
            continue

        try:
            again = input("\nDo you want to try again? (yes/no): ").strip().lower()
            if again != 'yes':
                print("Thank you!")
                break
        except Exception as e:
            print("An error occurred:", e)
            print("Exiting...")
            break

        
# Run the calculator
calculator()
