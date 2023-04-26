string = input("Enter a string: ")

upper_count = sum(1 for char in string if char.isupper())
lower_count = sum(1 for char in string if char.islower())

print("Number of upper case letters:", upper_count)
print("Number of lower case letters:", lower_count)