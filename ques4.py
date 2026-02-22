
# Importing datetime class from datetime module
# This is used to get the current date and year from the system
from datetime import datetime


# Function to calculate age and related time units
def age_calculator():
    try:
        # Taking birth year input from the user
        # Converting input into integer
        birth_year = int(input("Enter birth year: "))

        # Getting the current year from the system
        current_year = datetime.now().year  

        # Calculating age by subtracting birth year from current year
        age = current_year - birth_year

        # Displaying calculated age in years
        print("Age:", age)

        # Converting age into months (1 year = 12 months)
        print("Months:", age * 12)

        # Approximate days calculation (1 year ≈ 365 days)
        print("Days:", age * 365)

        # Converting age into hours (1 day = 24 hours)
        print("Hours:", age * 365 * 24)

        # Converting age into minutes (1 hour = 60 minutes)
        print("Minutes:", age * 365 * 24 * 60)

        # Calculating years remaining to reach 100 years
        print("Years until 100:", 100 - age)

    except:
        # If user enters invalid input (like letters instead of numbers)
        # This block handles the error and prevents program crash
        print("Invalid input")

if __name__=="__main__":
    age_calculator()