# Basic example of reusable function
def add(num1, num2):
    return int(num1) + (int(num2))
def subtract(num1, num2):
    return int(num1) + (int(num2))
def multiply(num1, num2):
    return int(num1) * (int(num2))
def divide(num1, num2):
    return int(num1) / (int(num2))

# Basic example of working with user input, printing to console and function invocation
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
print("Your result was: " + str(add(num1, num2)))

