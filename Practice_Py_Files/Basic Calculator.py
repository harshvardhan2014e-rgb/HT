def add_Numbers(num1, num2):
    return num1 + num2

def multiply_Numbers(num1, num2):
    return num1 * num2

def subtract_Numbers(num1, num2):
    return num1 - num2

def divide_Numbers(num1, num2):
    return num1 / num2

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

if choice == "1":
    print(number1 + number2)
elif choice == "2":
    print(number1 - number2)
elif choice == "3":
    print(number1 * number2)
elif choice == "4":
    print(number1 / number2)
else:
    print("Invalid choice")