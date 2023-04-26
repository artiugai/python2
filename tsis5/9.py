import re

string = input('Enter a string')
pattern = r'(?<!^)(?=[A-Z])'

result = re.sub(pattern, ' ', string)

print(result)