source_file = input("Enter the name 1st file: ")
destination_file = input("Enter the name of 2nd file: ")


with open(source_file, "r") as source, open(destination_file, "w") as destination:
 
    contents = source.read()

    destination.write(contents)

print(f"File {source_file} copied to {destination_file}")