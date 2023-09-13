from product import Product
from json import dumps, loads
import calendar
import time
import os 
import functools

# typed as int or float or str
def get_typed_input(prompt="Please enter a value: ", type='string'):
    try:
        # This will raise a ValueError exception if the value passed to the default input function is not a valid argument for the type function
        match type:
            case 'string':
                    input_val = input(prompt)
            case 'integer':
                    input_val = int(input(prompt))
            case 'float':
                  input_val = float(input(prompt))
            case _:
                  print("Program error, invalid type requested")
                  input_val = input(prompt)
    except ValueError:
        # Tell the user they have provided invalid input
        print(f"Invalid input. Please enter a value of type: {type.capitalize()}")
        # Use a recursive return to continue prompting until the correct type of value is inputted
        return get_typed_input(prompt)

    return input_val

def prompt_and_select_command(actions):
    for action in actions:
        print(action)
    return input(f"Run a command by typing {[*range(1, len(actions) + 1)]}: ")
    

def add_product(product_list):
    prod_name = get_typed_input('Enter product name: ')
    prod_price = get_typed_input('Enter product price: ', 'float')
    product_list.append(Product(prod_name, prod_price))

def display_products(product_list):
    for p in product_list:
        print(f"Product: {p.name}. Price: ${p.price}")

def product_to_dict(product):
     return product.as_dict()

def save_to_file(product_list):
    # TODO: Improve this function by preventing save if current and most recent version are the same as passed in product list.
    print("Saving to file...")
    product_save_list = list(map(product_to_dict, product_list))
    subdir = "product_inventory/product_files"  # name of the sub-directory 
    filename = "current.json"   # name of the file to create 
    # join the sub-directory and filename using os.path.join() 
    current_file_name = os.path.join(subdir, filename) 
    product_file_contents = open(current_file_name, 'r')
    json = dumps(product_save_list)
    # An attempt to verify that a change has been made to the list
    current_data = product_file_contents.read()
    product_file_contents.close()
    if current_data != json:
        product_file = open(current_file_name, 'w')
        product_file.write(json)
        product_file.close()

        # Save a version to retain history when current is overwritten 
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        subdir = "product_inventory/product_files/versions/"  # name of the sub-directory 
        filename = f"products-{time_stamp}.json"  # name of the file to create 
        # join the sub-directory and filename using os.path.join() 
        version_file_name = os.path.join(subdir, filename)
        version_file = open(version_file_name, 'w')
        version_file.write(json)
        version_file.close()
    print("Saved!")

def load_current_products():
    print("loading products")
    subdir = "product_inventory/product_files"  # name of the sub-directory 
    filename = "current.json"   # name of the file to create 
    # join the sub-directory and filename using os.path.join() 
    current_file_name = os.path.join(subdir, filename) 
    try:
        product_file = open(current_file_name, "r")
    except IOError:
        return []
    product_dict_json = product_file.read()
    if product_dict_json == "":
        return []
    product_dict_list = loads(product_dict_json)
    list_of_products = []
    for product in product_dict_list:
        list_of_products.append(Product(product['name'], product['price']))
    product_file.close()
    return list_of_products

def get_product_list_total(product_list):
    try:
        cost = functools.reduce(lambda a,b: a+b, [p.price for p in product_list])
    except TypeError:
        cost = 0
    print(f"The total cost for all products in the list is: ${cost}")