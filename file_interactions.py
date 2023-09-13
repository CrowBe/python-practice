number_list = open("my_number_list.txt", 'r')
my_numbers = number_list.read().splitlines()

sum = 0
for number in my_numbers:
    sum += int(number)

print(sum)

storage_file = open('my_data.txt', 'a')
data_to_save = input("What do you wish to save to file? ")
storage_file.write(data_to_save + '\n')
storage_file.close()

storage_file = open('my_data.txt', 'r')
my_lines = storage_file.read().splitlines()
print("You've currently saved these lines: ")
for line in my_lines:
    print(line)