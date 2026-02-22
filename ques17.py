# Function to check palindrome
def palindrome_checker():
    
    # Taking input from user (can be word or number)
    user_input = input("Enter word/number: ")

    # Display original input
    print("Original:", user_input)

    # Reverse the input using slicing
    reversed_input = user_input[::-1]

    # Display reversed version
    print("Reversed:", reversed_input)

    # For case-insensitive comparison (important for words)
    # Convert both original and reversed to lowercase
    if user_input.lower() == reversed_input.lower():
        print("Result: PALINDROME")
    else:
        print("Result: NOT A PALINDROME")


# Run the program
if __name__ == "__main__":
    palindrome_checker()