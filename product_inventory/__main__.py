from utils import prompt_and_select_command, add_product, display_products, save_to_file, load_current_products, get_product_list_total
# Application constants

running = True

actions = [
    "1. Add new product.",
    "2. List all products.",
    "3. Show product list total cost.",
    "4. Save products to file.",
    "5. Save products to file and exit the program.",
]

product_list = load_current_products()

# Application flow
def execute_command(command):
        running = True
        match command:
            case '1':
                add_product(product_list)
            case '2':
                display_products(product_list)
            case '3':
                get_product_list_total(product_list)
            case '4':
                save_to_file(product_list)
            case '5':
                save_to_file(product_list)
                running = False
            case 'quit':
                running = False
            case 'q':
                running = False
            case _:
                print('Invalid command, please try again.')
        return running

# Application execution
while running:
    print("Type 'quit' or 'q' to exit without saving.")
    running = execute_command(prompt_and_select_command(actions))