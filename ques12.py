# Function to print multiplication table
def multiplication_table():
    
    # Taking number input from user for which table will be printed
    n = int(input("Enter number: "))
    
    # Taking range input (how many multiples to print)
    r = int(input("Enter range: "))

    # Loop runs from 1 to r (inclusive)
    for i in range(1, r + 1):
        
        # Printing multiplication result using f-string formatting
        # Example: 5 x 1 = 5
        print(f"{n} x {i} = {n * i}")


# This ensures the function runs only when file is executed directly
if __name__ == "__main__":
    multiplication_table()