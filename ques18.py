# ------------------------------
# Arithmetic Operation Functions
# ------------------------------

# Function to add two numbers
def add(a, b):
    return a + b


# Function to subtract two numbers
def subtract(a, b):
    return a - b


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to divide two numbers
# Handles division by zero
def divide(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a / b


# Function to find modulus (remainder)
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero not allowed"
    return a % b


# Function to calculate power
def power(a, b):
    return a ** b


# ------------------------------
# Main Calculator Function
# ------------------------------
def calculator():
    
    while True:
        # Displaying menu
        print("\nCalculator Menu")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice: ")

        # Exit option
        if choice == "7":
            print("Exiting calculator...")
            break

        # For valid operation choices
        if choice in ["1", "2", "3", "4", "5", "6"]:
            
            # Taking two numbers from user
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            # Calling respective function based on user choice
            if choice == "1":
                result = add(a, b)

            elif choice == "2":
                result = subtract(a, b)

            elif choice == "3":
                result = multiply(a, b)

            elif choice == "4":
                result = divide(a, b)

            elif choice == "5":
                result = modulus(a, b)

            elif choice == "6":
                result = power(a, b)

            # Displaying result
            print("Result:", result)

        else:
            print("Invalid choice. Please try again.")


# Run the calculator
if __name__ == "__main__":
    calculator()