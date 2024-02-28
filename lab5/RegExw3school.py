#1 example
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
#2 example
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#3 example
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
#4 example
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
#5 example
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
#6 example
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#7 example
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
#8 example
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#9 example
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
#10 example
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
#11 example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#12 example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#13 example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
