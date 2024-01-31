#1 example
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2 example
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#3 example
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#4 example
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#5 example
list1 = ["abc", 34, True, 40, "male"]
#6 example
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#7 example
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#8 example
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#9 example
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#10 example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#11 example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#12 example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#13 example
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#14 example
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#15 example
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#16 example
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#17 example
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#18 example
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#19 example
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#20 example
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#21 example
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#22 example
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#23 example
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#24 example
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#25 example
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#26 example
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#27 example
thislist = ["apple", "banana", "cherry"]
del thislist
#28 example
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#29 example
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#30 example
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#31 example
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#32 example
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#33 example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#34 example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#35 example
newlist = [x for x in fruits if x != "apple"]
#36 example
newlist = [x for x in fruits]
#37 example
newlist = [x for x in range(10)]
#38 example
newlist = [x for x in range(10) if x < 5]
#39 example
newlist = [x.upper() for x in fruits]
#40 example
newlist = ['hello' for x in fruits]
#41 example
newlist = [x if x != "banana" else "orange" for x in fruits]
#42 example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#43 example
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#44 example
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#45 example
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#46 example
def myfunc(n):
  return abs(n - 50)
#47 example
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#48 example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#49 example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#50 example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#51 example
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#52 example
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#53 example
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#54 example
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#55 example
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)