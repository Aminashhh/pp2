#1 example
def greeting(name):
  print("Hello, " + name)
#2 example
import mymodule

mymodule.greeting("Jonathan")
#3 example
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#4 example
import mymodule

a = mymodule.person1["age"]
print(a)
#5 example
import mymodule as mx

a = mx.person1["age"]
print(a)
#6 example
import platform

x = platform.system()
print(x)
#7 example
import platform

x = dir(platform)
print(x)
#8 example
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
#9 example
from mymodule import person1

print (person1["age"])
