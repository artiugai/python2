import os

path = input("Enter path: ")

if os.path.exists(path):
    head, tail = os.path.split(path)
    print(f"Filename: {tail}")
    print(f"Directory: {head}")
else:
    print("Path does not exist.")