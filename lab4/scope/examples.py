#1 example
def myfunc():
  x = 300
  print(x)

myfunc()
#2 example
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
#3 example
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
#4 example
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
#5 example
def myfunc():
  global x
  x = 300

myfunc()

print(x)
#6 example
def myfunc():
  global x
  x = 300

myfunc()

print(x)