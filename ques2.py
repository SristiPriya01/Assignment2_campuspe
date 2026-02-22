# Q2: Simple Calculator
# Performs basic arithmetic operations
def simple_calculator():
    try:
        # Taking user input
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        # Performing operations
        print(f"{a} + {b} = {a+b}")
        print(f"{a} - {b} = {a-b}")
        print(f"{a} * {b} = {a*b}")

        # Checking division by zero
        if b != 0:
            print(f"{a} / {b} = {a/b:.2f}")
            print(f"{a} % {b} = {a%b}")
        else:
            print("Division and modulus not possible (division by zero)")

        print(f"{a} ^ {b} = {a**b}")

    except:
        print("Invalid input")
if __name__ == "__main__":
    simple_calculator()