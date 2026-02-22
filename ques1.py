def personal_bio_card():
    # Storing student details in variables
    name = "Srishti Priya"
    age = 21
    course = "Python Programming"
    college = "Your College Name"
    email = "your_email@example.com"

    # Printing formatted bio card using box style
    print("╔════════════════════════════════╗")
    print("║       STUDENT BIO CARD        ║")
    print("╠════════════════════════════════╣")
    print(f"║ Name    : {name:<18}║")
    print(f"║ Age     : {age} years{'':<10}║")
    print(f"║ Course  : {course:<18}║")
    print(f"║ College : {college:<18}║")
    print(f"║ Email   : {email:<18}║")
    print("╚════════════════════════════════╝")

    # Calling the function so it executes
if __name__ == "__main__":
    personal_bio_card()