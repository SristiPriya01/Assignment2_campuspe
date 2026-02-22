# Function to convert temperature between Celsius and Fahrenheit
def temperature_converter():

    # Infinite loop so menu keeps running until user chooses Exit
    while True:

        # Displaying menu options
        print("\n1. C to F\n2. F to C\n3. Exit")

        # Taking user choice as input
        choice = input("Choice: ")

        # If user selects option 1 → Celsius to Fahrenheit
        if choice == "1":

            # Taking temperature in Celsius from user
            c = float(input("Enter Celsius: "))

            # Applying formula: (C × 9/5) + 32
            # This converts Celsius into Fahrenheit
            print("Fahrenheit:", (c * 9/5) + 32)

        # If user selects option 2 → Fahrenheit to Celsius
        elif choice == "2":

            # Taking temperature in Fahrenheit from user
            f = float(input("Enter Fahrenheit: "))

            # Applying formula: (F - 32) × 5/9
            # This converts Fahrenheit into Celsius
            print("Celsius:", (f - 32) * 5/9)

        # If user selects option 3 → Exit program
        elif choice == "3":

            # break statement stops the loop and exits function
            break


# Ensures function runs only when file is executed directly
if __name__ == "__main__":
    temperature_converter()