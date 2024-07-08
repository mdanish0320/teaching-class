# create date time from integer
from datetime import date, datetime

my_day = 26
my_month = 8
my_year = 2023
d = date(
  day=26, 
  month=8, 
  year=2023
)
print("create datetime from integer")
print(d)
print(d.year)


# create date time from timestamp - number of seconds from 1970-Jan-01
ts = 1693029240 # number of seconds
ts_date = datetime.fromtimestamp(ts)
print("\ncreate datetime from timestamp")
print(ts_date)
print(ts_date.year)
