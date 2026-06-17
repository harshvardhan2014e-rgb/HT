# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Performing calculations
sum_result = add_numbers(number1, number2)
product_result = multiply_numbers(number1, number2)

# Displaying results
print(f"The sum is: {sum_result}")
print(f"The product is: {product_result}")
