#1 example
a = 33
b = 200
if b > a:
  print("b is greater than a")
#2 example
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#3 example
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#4 example
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if a > b: print("a is greater than b")
#5 example
a = 2
b = 330
print("A") if a > b else print("B")
#6 example
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#7 example
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#8 example
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#9 example
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#10 example
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#11 example
a = 33
b = 200

if b > a:
  pass