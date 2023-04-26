import string
import os

directory = "./Desktop/"

if not os.path.exists(directory):
    os.makedirs(directory)

for letter in string.ascii_uppercase:
    filename = directory + letter + ".txt"
    
    with open(filename, "w") as file:
        file.write("This is file " + letter + ".txt\n")
    
    print("Created file", filename)