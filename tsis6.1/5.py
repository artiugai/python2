path = input("Enter path to file: ")

my_list = input("Enter list of items, separated by commas: ").split(",")

with open(path, 'w') as file:

    for item in my_list:

        file.write(item.strip() + '\n')