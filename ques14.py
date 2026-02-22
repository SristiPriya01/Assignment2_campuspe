# Function to calculate factorial of a number
def factorial_calc():
    
    # Taking integer input from user
    n = int(input("Enter number: "))

    # Factorial is not defined for negative numbers
    if n < 0:
        print("Not possible")
        return   # Exit the function immediately

    # Initialize factorial value as 1
    # (Because factorial multiplication starts from 1)
    fact = 1

    # Loop runs from 1 to n (inclusive)
    for i in range(1, n + 1):
        
        # Multiply current value of fact with i
        # This keeps updating factorial value
        fact *= i

    # Print the final factorial result
    print("Factorial:", fact)


# Ensures function runs only when file is executed directly
if __name__ == "__main__":
    factorial_calc()