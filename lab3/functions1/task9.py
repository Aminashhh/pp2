import math

def volume(radius):

    if radius < 0:
        return 

    volume = (4 / 3) * math.pi * radius**3
    return int(volume)


radius_input = int(input())
result = volume(radius_input)
print(f"{radius_input} = {result}")

