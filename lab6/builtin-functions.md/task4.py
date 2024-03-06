import time
import math

def square(number, milliseconds):
    time.sleep(milliseconds/1000)
    square_root= math.sqrt(number)
    return square_root

number= 25100
milliseconds = 2123
result = square(number, milliseconds)
print(f"Square root of {number} after {milliseconds} miliseconds is {result}")