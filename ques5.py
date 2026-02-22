# Function to split restaurant bill including tax and tip
def bill_splitter():
    try:
        # Taking total bill amount from user
        # Converted to float to allow decimal values
        bill = float(input("Enter total bill: "))

        # Taking number of people sharing the bill
        # Converted to integer since number of people must be whole number
        people = int(input("Number of people: "))

        # Taking tax percentage input
        tax_percent = float(input("Tax percentage: "))

        # Taking tip percentage input
        tip_percent = float(input("Tip percentage: "))

        # Calculating tax amount
        # Formula: (bill × tax percentage) / 100
        tax = bill * tax_percent / 100

        # Adding tax to original bill
        after_tax = bill + tax

        # Calculating tip on amount after tax
        tip = after_tax * tip_percent / 100

        # Final total amount including tax and tip
        total = after_tax + tip

        # Calculating how much each person has to pay
        per_person = total / people

        # Displaying formatted bill breakdown
        print("\n=== BILL BREAKDOWN ===")
        print("Subtotal:", bill)
        print("Tax:", tax)
        print("After tax:", after_tax)
        print("Tip:", tip)
        print("Total:", total)
        print("Per person:", per_person)

    except:
        # If user enters invalid input (like text instead of numbers)
        # This prevents program from crashing
        print("Invalid input")


# This ensures the function runs only when the file is executed directly
if __name__ == "__main__":
    bill_splitter()