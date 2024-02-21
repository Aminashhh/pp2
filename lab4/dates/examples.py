#1 example
import datetime

x = datetime.datetime.now()
print(x)
#2 example
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))
#3 example
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
#4 example
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))
