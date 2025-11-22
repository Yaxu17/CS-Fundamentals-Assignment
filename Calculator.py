# Simple Calculator Program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)\n")

choice = input("Enter your choice (1-4): ")

# Performing operations
if choice == "1":
    result = num1 + num2
    print("Result:", num1, "+", num2, "=", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", num1, "-", num2, "=", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", num1, "*", num2, "=", result)

elif choice == "4":
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("Result:", num1, "/", num2, "=", result)

else:
    print("Invalid choice.")
