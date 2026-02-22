# Function to calculate sum, average, maximum and minimum
def sum_average():
    
    # Taking input for how many numbers user wants to enter
    count = int(input("How many numbers: "))
    
    # Creating an empty list to store numbers
    nums = []

    # Loop runs 'count' times to take numbers from user
    for i in range(count):
        
        # Taking each number as float and adding it to the list
        nums.append(float(input("Enter number: ")))

    # Calculating and printing the total sum of numbers
    print("Sum:", sum(nums))
    
    # Calculating and printing average (sum divided by count)
    print("Average:", sum(nums) / count)
    
    # Printing maximum value from the list
    print("Max:", max(nums))
    
    # Printing minimum value from the list
    print("Min:", min(nums))


# This ensures the function runs only when file is executed directly
if __name__ == "__main__":
    sum_average()