import re

string = input("Enter a string: ")

pattern = '[a-z]+_[a-z]+'

matches = re.findall(pattern, string)

print(matches)
