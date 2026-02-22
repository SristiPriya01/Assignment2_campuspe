import math


# 1. Factorial Function
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# 2. Prime Check Function
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


# 3. Fibonacci Function (nth term)
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 4. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))


# 5. Reverse Number
def reverse_number(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num


# 6. Armstrong Number Check
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n


# 7. Greatest Common Divisor (Euclidean Algorithm)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


# 8. Least Common Multiple
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


# 9. Perfect Number Check
def is_perfect_number(n):
    if n <= 1:
        return False
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n


# 10. Menu Function
def math_menu():
    while True:
        print("\nNumber System Menu")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "10":
            print("Exiting...")
            break

        elif choice == "1":
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))

        elif choice == "2":
            n = int(input("Enter number: "))
            print("Prime:", is_prime(n))

        elif choice == "3":
            n = int(input("Enter n: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == "4":
            n = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(n))

        elif choice == "5":
            n = int(input("Enter number: "))
            print("Reversed number:", reverse_number(n))

        elif choice == "6":
            n = int(input("Enter number: "))
            print("Armstrong:", is_armstrong(n))

        elif choice == "7":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == "8":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == "9":
            n = int(input("Enter number: "))
            print("Perfect Number:", is_perfect_number(n))

        else:
            print("Invalid choice")


# Run the menu
if __name__ == "__main__":
    math_menu()