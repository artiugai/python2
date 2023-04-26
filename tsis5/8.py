import re

string = input('Enter a string: ')

pattern = '[A-Z][^A-Z]*'

result = re.findall(pattern, string)

print(result)