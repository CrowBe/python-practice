# Basic example of reusable functions
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

# More complex, recursive function that extends an existing function for use in a small program
def get_number_input(prompt="Please type a number"):
    try:
        # This will raise a ValueError exception if the value passed to the default input function is not a valid argument for the int() function
        num_input = int(input(prompt))
    except ValueError:
        # Tell the user they have provided invalid input
        print("Invalid input. Please enter a value using characters 0-9.")
        # Use a recursive return to continue prompting until the correct type of value is inputted
        return get_number_input(prompt)

    return num_input