def parallelogram_area(base, height):
    area = base * height
    return area

base_length = float(input(" "))
height = float(input(" "))

area = parallelogram_area(base_length, height)
print(" ", area)