#1 example
x = lambda a : a + 10
print(x(5))
#2 example
x = lambda a, b : a * b
print(x(5, 6))
#3 example
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#4 example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#5 example
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
#6 example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

