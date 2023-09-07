# Review basic boolean checks statements
x = 10
y = 20
z = 10
print(x,y,z)
print('item 0 == item 2', x == z)
print('item 0 == item 1', x == y)
print('item 0 >= item 1', x >= y)
print('item 0 <= item 1', x <= y)

# Basic conditionals checking
if x == y:
    print("This should never run")
else:
    print("This is an else that should always run")

if y > x:
    print("We expect this to run because 20 is greater than 10")
else:
    print("We don't expect this to run")

if x == 1:
    print("This shouldn't run")
elif x == 10:
    print("X is equal to 10")

# Combining functions, conditions and inputs to demonstrate the purpose of conditionals in a program
def add(num1, num2):
    return int(num1) + (int(num2))
def subtract(num1, num2):
    return int(num1) + (int(num2))
def multiply(num1, num2):
    return int(num1) * (int(num2))
def divide(num1, num2):
    return int(num1) / (int(num2))
# Set up variables for our program using input
num1 = input("Please enter a number: ")
num2 = input("Please enter a second number: ")
operator = input("Please select an operation to perform with your numbers: [add, subtract, divide, multiply]: ")
# use a series of conditionals to check which function to call. An else condition catches invalid input.
if operator == 'add':
    result = add(num1, num2)
elif operator == 'subtract':
    result = subtract(num1, num2)
elif operator == 'multiply':
    result = multiply(num1, num2)
elif operator == 'divide':
    result = divide(num1, num2)
else:
    result = "Operator selection error"
    
print("Your result is: " + str(result))
