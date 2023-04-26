path = input("Enter path to text file: ")


line_count = 0


with open(path, "r") as file:

    for line in file:

        line_count += 1

print(f"The file has {line_count} lines.")