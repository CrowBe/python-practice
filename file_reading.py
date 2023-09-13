number_list = open("my_number_list.txt", 'r')
my_numbers = number_list.read().splitlines()

sum = 0
for number in my_numbers:
    sum += int(number)

print(sum)