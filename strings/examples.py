#1 example
print("Hello")
print('Hello')
#2 example
a = "Hello"
print(a)
#3 example
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#4 example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#5 example
a = "Hello, World!"
print(a[1])
#6 example
for x in "banana":
  print(x)
#7 example
a = "Hello, World!"
print(len(a))
#8 example
txt = "The best things in life are free!"
print("free" in txt)
#9 example
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
#10 example
txt = "The best things in life are free!"
print("expensive" not in txt)
#11 example
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#12 example
b = "Hello, World!"
print(b[2:5])
#13 example
b = "Hello, World!"
print(b[:5])
#14 example
a = "Hello, World!"
print(a.upper())
#15 example
a = "Hello, World!"
print(a.lower())
#16 example
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#17 example
a = "Hello"
b = "World"
c = a + b
print(c)
#18 example
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#19 example
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#20 example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#21 example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#22 example
txt = "We are the so-called \"Vikings\" from the north."
