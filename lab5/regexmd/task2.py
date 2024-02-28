import re
txt = input((" "))
x = re.findall("a{1}b{2,3}",txt)
print(x)