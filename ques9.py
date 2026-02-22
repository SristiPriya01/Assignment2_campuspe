# Function to calculate movie ticket price based on age and day
def ticket_pricing():

    # Taking age input from user (converted to integer)
    age = int(input("Enter age: "))

    # Taking day of week input and converting to lowercase
    # This ensures case-insensitive comparison (e.g., Friday, FRIDAY, friday)
    day = input("Enter day: ").lower()
    # Taking number of tickets (must be whole number)
    tickets = int(input("Enter number of tickets: "))
    # Determining ticket price based on age
    if age < 3:
        price = 0              # Free for children below 3

    elif age <= 12:
        price = 150            # Child price

    elif age <= 59:
        price = 300            # Adult price

    else:
        price = 200            # Senior citizen price

    # Calculating total price before discount
    total = price * tickets
    # Applying weekend discount
    # 20% discount for Friday, Saturday, Sunday
    if day in ["friday", "saturday", "sunday"]:
        discount = total * 0.2   # 20% of total
    else:
        discount = 0             # No discount on weekdays

    # Printing final amount after discount
    print("Total:", total - discount)
# Ensures function runs only when file is executed directly
if __name__ == "__main__":
    ticket_pricing()