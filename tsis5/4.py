import re

string = input("Enter a string: ")

pattern = '[A-Z][a-z]+'

matches = re.findall(pattern, string)


print(matches)
