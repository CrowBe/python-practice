# More class inheritance practice
class Contact:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_info = first_name + ' ' + last_name

    def print_contact_information(self):
        print(self.full_info)

class EmailContact(Contact):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name)
        self.email = email
        self.full_info = email