# Function to calculate total marks, percentage, grade and result
def grade_calculator():

    # Creating an empty list to store marks of 5 subjects
    marks = []

    # Loop runs 5 times to take marks for 5 subjects
    for i in range(5):
        # Taking input for each subject
        # Converting input to float to allow decimal marks
        m = float(input(f"Enter marks for subject {i+1}: "))
        
        # Adding each subject's marks to the list
        marks.append(m)

    # Calculating total marks using sum() function
    total = sum(marks)

    # Calculating percentage
    # Since total marks are out of 500, dividing by 5 gives percentage
    percentage = total / 5

    # Determining grade based on percentage using conditional statements
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Checking pass or fail condition
    # Student must score at least 40 in ALL subjects to pass
    # all() function checks if condition is True for every subject
    result = "Pass" if all(m >= 40 for m in marks) else "Fail"

    # Displaying results
    print("Total:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Result:", result)


# This ensures the function runs only when the file is executed directly
if __name__ == "__main__":
    grade_calculator()