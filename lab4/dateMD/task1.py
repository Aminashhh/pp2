from datetime import datetime,timedelta

x = datetime.now()
result=x-timedelta(days=5)
print(result)