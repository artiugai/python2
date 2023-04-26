from functools import reduce

def multiply_list(numbers):
    result = reduce((lambda x, y: x * y), numbers)
    return result

input_str = input("Enter numbers with space: ")

numbers = [int(n) for n in input_str.split()]

result = multiply_list(numbers)

print("result:", result)
