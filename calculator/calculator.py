import os
import math

print("==============================")
print("      PYTHON CALCULATOR")
print("==============================")

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Square Root")

choice = input("\nEnter your choice (1-6): ")

if choice == "1":
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    result = num1 + num2
    print(f"Result: {result}")

elif choice == "2":
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    result = num1 - num2
    print(f"Result: {result}")

elif choice == "3":
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))
    result = num1 * num2
    print(f"Result: {result}")

elif choice == "4":
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"Result: {result}")

elif choice == "5":
    num1 = float(input("Enter Number 1: "))
    num2 = float(input("Enter Number 2: "))

    if num2 == 0:
        print("Error: Cannot modulo by zero")
    else:
        result = num1 % num2
        print(f"Result: {result}")

elif choice == "6":
    num1 = float(input("Enter Number: "))

    if num1 < 0:
        print("Error: Cannot calculate square root of a negative number")
    else:
        result = math.sqrt(num1)
        print(f"Result: {result}")

else:
    print("Invalid choice")

