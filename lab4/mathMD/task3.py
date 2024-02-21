import math

print("Input the nuber of sides:")
n=int(input(" "))
print("Input the length of a side:")
x=int(input(" "))
result=(n*(pow(x,2)))/(4 * math.tan(math.pi/n))
print(int(result))