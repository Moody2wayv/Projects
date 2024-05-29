import math

# Define four functions for adding, multiplying, and subtraction.
def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    return result

# Print the menu and ask the user to select an option.
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Previous calculations")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        if choice == '5':
            with open(".venv/equations.txt", "r") as file:
                for line in file:
                    print(line.strip())
            print("Previous calculations:")
        else:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if num1 < 0 or num2 < 0:
                    raise ValueError("Error: Negative numbers are not allowed.")
            except ValueError as e:
                print(e)
                continue

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                else:
                    print("Result:", divide(num1, num2))
    else:
        print("Invalid input. Please enter a valid option.")
