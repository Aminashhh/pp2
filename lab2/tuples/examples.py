#1 example
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#2 example
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#3 example
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#4 example
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#5 example
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#6 example
tuple1 = ("abc", 34, True, 40, "male")
#7 example
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#8 example
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#9 example
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#10 example
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#11 example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#12 example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#13 example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#14 example
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#15 example
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#16 example
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#17 example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#18 example
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#19 example
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#20 example
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
#21 example
fruits = ("apple", "banana", "cherry")
#22 example
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#23 example
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#24 example
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#25 example
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#26 example
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#27 example
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#28 example
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#29 example
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

