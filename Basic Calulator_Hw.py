def add_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def subtract_numbers(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def average_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

print("Welcome to the Python Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Average")

choice = input("Enter choice (1/2/3/4): ")

numbers = []
count = int(input("Enter How many Numbers do you want to add: "))
i = 1
while i <= count:
    print("Enter number", i, ":")
    num = int(input())
    numbers.append(num)
    i = i + 1

if choice == "1":
    print("Sum =", add_numbers(numbers))
elif choice == "2":
    print("Difference =", subtract_numbers(numbers))
elif choice == "3":
    print("Product =", multiply_numbers(numbers))
elif choice == "4":
    print("Average =", average_numbers(numbers))
else:
    print("Invalid choice")
