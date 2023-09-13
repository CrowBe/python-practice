# Exception handling
# Raising exceptions with custom message:
# raise IndexError('A custom message I want to pass to my error handling')
# Custom exceptions
class MyError(Exception):
    pass
for num in [1,2,3,4,5]:
    # Specific condition that you care about
    try:
        print(num)
        if num == 3:
            raise MyError
    except MyError:
        print("We raised my specific error")

my_list = [0,1,2]
# This is an example of catching any exception, to guarantee the program does not halt execution
for item in [1,2,3,4,5]:
    try:
        print(my_list[item])
        # THIS IS A BAD IDEA, the unspecific except will obscure any other, unintended exceptions.
    except:
        print('This index is outside the list range')

# Demonstrate how you can catch specific exceptions to prevent program halting
for item in [1,2,3,4,5]:
    try:
        print(my_list[item])
    except IndexError:
        print('This index is outside the list range')

# Demonstrate how you can ensure that errors not specifically excepted will still halt program execution
my_dict = {'a': 3}
for item in [1,2,3,4,5]:
    try:
        # This will throw a key error as 1 is not a key of my_dict
        print(my_dict[item])
    except IndexError:
        print('This index is outside the list range')



# Common Exceptions

# IndexError: list index out of range
# failing = my_list[3]

# KeyError: 'key'
# my_dict['b']

# Demonstrate how exceptions will halt program execution
for item in [1,2,3,4,5]:
    # This will trigger the same exception as seen on line 5 and halt execution before iterating through 4,5
    print(my_list[item])
