# Basic while loop
print_number = 3
while print_number > 0:
    print("Hello World ", print_number)
    print_number -= 1

# Basic list looping
all_nums = [1,2,3]
for num in all_nums:
    print("Hello World ", num)
# String looping
long_string = "Hello World"
for char in long_string:
    print(char)
# Loop through dictionary keys
all_key_vals = {1: "One", 2: "Two", 3: "Three"}
for key in all_key_vals:
    print(key, " as a word: ", all_key_vals[key])

# Function that uses looping to sum numbers in a list
# Basic looping in a function
def sum_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total 
print(sum_list([1,2,3,4, -5]))

# Basic looping with a break statement
def list_contains(my_list, target_element):
    result = "No"
    for el in my_list:
        if el == target_element:
            result = "Yes"
            break
    return result

print("Contains: ", list_contains([2,4,6,78,9], 8))
print("Contains: ", list_contains([2,4,6,78,9], 4))
# Basic looping with a continue statement
def print_all_even_nums(my_list):
    for num in my_list:
        if num % 2 == 0:
            print(num)

print_all_even_nums([1,2,3,4,5,6])
# List comprehension for shorter syntax
def square_list_nums(my_list):
    return [num * num for num in my_list]

print(square_list_nums([1,2,3,4]))