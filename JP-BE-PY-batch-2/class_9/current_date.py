# play with current date and datetime
from datetime import date, datetime

# ISO (International Organization for Standardization) Date format
# 2023-08-26 10:30:00+05:00
# %Y-%m-%d %H:%M:%S%z

# date
print("date")
current_date = date.today()
print(current_date) # %Y-%m-%d
print(current_date.year)
print(current_date.month)
print(current_date.day)

# date with time -> system local time
print("\ndate with time - local sytem")
current_date_time = datetime.now() # system localtime
print(current_date_time)  # %Y-%m-%d %H:%M:%S.%f

print(current_date_time.year)
print(current_date_time.month)
print(current_date_time.day)
print(current_date_time.hour)
print(current_date_time.minute)
print(current_date_time.second)

# date with time -> UTC datetime without timezone
print("\ndate with time - UTC")
utc_date_time = datetime.utcnow()  # system localtime
print(utc_date_time)  # %Y-%m-%d %H:%M:%S.%f
