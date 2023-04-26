import os

path = input("Enter path: ")

if not os.path.exists(path):
    print("Path does not exist.")
else:
    if os.access(path, os.R_OK):
        print("Read access: Yes")
    else:
        print("Read access: No")

    if os.access(path, os.W_OK):
        print("Write access: Yes")
    else:
        print("Write access: No")

    if os.access(path, os.X_OK):
        print("Execute access: Yes")
    else:
        print("Execute access: No")