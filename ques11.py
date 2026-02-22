# Function to print number pattern
def pattern1(n):
    
    # Outer loop controls number of rows
    # It runs from 1 to n (inclusive)
    for i in range(1, n + 1):
        
        # Inner loop prints numbers in each row
        # It prints numbers from 1 up to current row number (i)
        for j in range(1, i + 1):
            print(j, end=" ")   # end=" " keeps numbers on same line with space
        
        # After printing one row, move to next line
        print()


# This ensures the function runs only when file is executed directly
if __name__ == "__main__":
    
    # Taking height input from user
    height = int(input("Enter height: "))
    
    # Calling the pattern function with user input
    pattern1(height)