import time
import math

number = int(input("Enter a number: "))
delay = int(input("Enter the delay in milliseconds: "))

delay_secs = delay / 1000

time.sleep(delay_secs)

sqrt_number = math.sqrt(number)

print(f"Square root of {number} after {delay} milliseconds is {sqrt_number}")