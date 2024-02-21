from datetime import datetime

date1_str = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

difference_seconds = abs((date2 - date1).total_seconds())

print(difference_seconds)