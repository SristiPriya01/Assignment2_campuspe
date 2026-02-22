# Function to check whether a given year is a leap year
def leap_year_checker():

    # Taking year input from the user
    # Converting input to integer
    year = int(input("Enter year: "))

    # Rule 1:
    # If a year is divisible by 400 → It IS a leap year
    if year % 400 == 0:
        print("Leap year (divisible by 400)")

    # Rule 2:
    # If a year is divisible by 100 but NOT by 400 → NOT a leap year
    elif year % 100 == 0:
        print("Not leap year (divisible by 100)")

    # Rule 3:
    # If a year is divisible by 4 but NOT by 100 → It IS a leap year
    elif year % 4 == 0:
        print("Leap year (divisible by 4)")

    # If none of the above conditions are satisfied → Not a leap year
    else:
        print("Not leap year")


# Ensures the function runs only when the file is executed directly
if __name__ == "__main__":
    leap_year_checker()