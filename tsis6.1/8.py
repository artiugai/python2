import os

file_path = input("Enter the path to the file to be deleted: ")

if os.access(file_path, os.F_OK | os.R_OK | os.W_OK):
    os.remove(file_path)
    print(f"{file_path} deleted successfully.")
else:
    print(f"{file_path} does not exist or is not accessible.")