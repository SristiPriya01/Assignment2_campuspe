import math   # Importing math module for square root function
# Function to check whether a single number is prime

def is_prime(n):
    
    # Prime numbers are greater than 1
    # Negative numbers, 0 and 1 are not prime
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # If number is divisible by 2 and greater than 2, it is not prime
    if n % 2 == 0:
        return False

    # Check divisibility from 3 up to square root of n
    # We use sqrt(n) because a larger factor would already have a smaller pair
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False   # If divisible, not prime

    return True   # If no divisors found, number is prime
# Part 1: Check single number
def check_single_number():
    
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")

# Part 2: Find prime numbers in a given range
def primes_in_range():
    
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    prime_list = []   # Empty list to store prime numbers

    # Loop through each number in the range
    for number in range(start, end + 1):
        if is_prime(number):
            prime_list.append(number)

    # Display result
    print("Prime numbers:", ", ".join(map(str, prime_list)))

# Main Program
if __name__ == "__main__":
    
    # Run Part 1
    check_single_number()
    
    # Run Part 2
    primes_in_range()