#1 example
def my_function():
  print("Hello from a function")
#2 example
def my_function():
  print("Hello from a function")

my_function()
#3 example
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#4 example
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#5 example
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#6 example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#7 example
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#8 example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#9 example
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#10 example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#11 example
def myfunction():
  pass
#12 example
def my_function(x, /):
  print(x)

my_function(3)
#13 example
def my_function(x):
  print(x)

my_function(x = 3)
#14 example
def my_function(*, x):
  print(x)

my_function(x = 3)
#15 example
def my_function(x):
  print(x)

my_function(3)
#16 example
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
#17 example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)