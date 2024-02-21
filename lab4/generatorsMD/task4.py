a = int(input(" "))
b = int(input(" "))
def squares(a, b):
    return (num ** 2 for num in range(a, b + 1))
print("Squares of numbers from", a, "to", b)
for square in squares(a, b):
    print(square)