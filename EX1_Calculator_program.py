# python exercise program to make a simple calculator
# This program adds, subtracts, multiplies and divides two numbers

# take input from the user
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.remainder")
print("6.floor division")
print("7.exponent")

choice = input("Enter choice(1/2/3/4/5/6/7):")

if(choice in ('1', '2', '3', '4', '5', '6', '7')):
    if choice == '1':
        print(num1, "+", num2, "=", (num1 + num2))

    elif choice == '2':
        print(num1, "-", num2, "=", (num1 - num2))

    elif choice == '3':
        print(num1, "*", num2, "=", (num1 * num2))

    elif choice == '4':
        print(num1, "/", num2, "=", (num1 / num2))
    elif choice == '5':
        print(num1, "%", num2, "=", (num1 % num2))
    elif choice == '6':
        print(num1, "//", num2, "=", (num1 // num2))
    elif choice == '7':
        print(num1, "**", num2, "=", (num1 ** num2))
else:
    print("Invalid input")
# --- IGNORE ---
# day3 content added