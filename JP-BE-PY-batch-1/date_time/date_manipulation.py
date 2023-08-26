# pip install python-dateutil
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# date manipulation using replace method of date object
print("date manipulation using replace method of date object")
dt = "2023-01-01 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print("original_date:", dt_obj)

updated_date = dt_obj.replace(year=2000, month=5, day=10)
print("updated_date:", updated_date)






# date manipulation using timedelta
print("\ndate manipulation using timedelta")
dt = "2023-01-01 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print("original_date:", dt_obj)
updated_date = dt_obj - timedelta(days=2)
print("updated_date:", updated_date)


# generate new dates
dt = "2023-01-05 23:59:59"
dt_obj = datetime.fromisoformat(dt)
print(f"\ngenerate past dates from this date:\n{dt_obj}")

for i in range(1, 10):
    change_dt = dt_obj - timedelta(days=i)
    print("loop", change_dt)


# date manipulation using relativedelta to change year, month and day easily
print("\ndate manipulation using relativedelta to change year, month and day easily")
dt_1 = datetime.now()
print(dt_1)

x = dt_1 - relativedelta(months=2, year=1)
print(x)


dt_2 = datetime.now()
x = dt_2 + relativedelta(months=2, hours=2, days=4)
print(x)


# difference between timedelta and relativedelta
"""
timedelta deals with day and smaller units i.e day, hour, minute, second etc
relativedelta deals with units years, months, days
"""


# calculate difference between 2 dates
print("\ncalculate difference between 2 dates")
current_dt = datetime.now()
custom_dt = datetime.now()

custom_dt = custom_dt.replace(day=2)

print(custom_dt)
print(current_dt)

diff = current_dt - custom_dt
print(diff.days)
print(diff.total_seconds())


