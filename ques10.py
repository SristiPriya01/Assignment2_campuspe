# Function to simulate a simple ATM system
def atm():

    # Initial balance set to ₹10,000
    balance = 10000

    # Infinite loop so ATM keeps running until user chooses Exit
    while True:

        # Displaying ATM menu options
        print("\n1.Check Balance\n2.Deposit\n3.Withdraw\n4.Exit")

        # Taking user choice
        choice = input("Choice: ")
        # Option 1: Check Balance
        
        if choice == "1":
            # Displays current balance
            print("Balance:", balance)
        # Option 2: Deposit Money
       
        elif choice == "2":
            # Taking deposit amount
            amount = float(input("Enter amount: "))
            # Adding deposit amount to balance
            balance += amount  
        # Option 3: Withdraw Money
        elif choice == "3":
            # Taking withdrawal amount
            amount = float(input("Enter amount: "))

            # Checking minimum balance rule
            # At least ₹500 must remain after withdrawal
            if balance - amount >= 500:
                balance -= amount   # Deduct amount
            else:
                print("Minimum balance required")
        # Option 4: Exit ATM
      
        elif choice == "4":
            # break stops the loop and exits ATM
            break


# Ensures function runs only when file is executed directly
if __name__ == "__main__":
    atm()