from datetime import date, datetime

# why we need date module
# dt = "07-07-2024"

# dt_parts = dt.split("-")
# dt_parts[1] = "08"

# dt = "".join(dt_parts) 

# current date
today = date.today()
print(today, type(today))
print(today.year)
print(today.month)
print(today.day)

# current date with time
dt_now = datetime.now()
print(dt_now, type(dt_now))
print(dt_now.hour)
print(dt_now.minute)
print(dt_now.second)

# create date from string
dt = "2024-07-06" # ISO format date
dt = date.fromisoformat(dt)
print(dt, type(dt))

# dt = "06-07-2024" # ISO format date
# dt = date.fromisoformat(dt) # it will raise error
# print(dt, type(dt))

dt = "06-danish-07-2024" # ISO format date
dt = datetime.strptime(dt, "%d-danish-%m-%Y") # it will raise error
print(dt, type(dt))
print(dt.date())

# create date from int

# dt = date( month=1, year=2024, day=6)
# print(dt)
# dt = date(1, 2024, 6)
# print(dt)

# datetime strptime
dt_n = "2024-07-06 12:38:00"
dt_obj = datetime.strptime(dt_n, "%Y-%m-%d %H:%M:%S")
print(dt_obj)

# convert date object to string
dt = datetime.now()
pak_dt = dt.strftime("%d-%m-%Y")
print(pak_dt, type(pak_dt))


dt_str = "2024-07-06 10:10:00"
dt_obj = datetime.fromisoformat(dt_str)
pak_dt = dt_obj.strftime("%d-%m-%Y %I:%M:%S %p")
print(pak_dt, type(pak_dt))

# date manipulation

# def greeting(username, greeting_type):
#     pass


# greeting(greeting_type="hi", username="danish")
# greeting("hi", "danish")
# greeting("danish", "hi")

# string     -> dateobject # strptime
# dateobject -> string # strftime

"""
**Task:**
1. Write a function `parse_iso_date(iso_str)` that takes an ISO format date string 
(e.g., '2023-07-06T12:34:56') and returns a `datetime` object.
"""

# def parse_iso_date(iso_str):
#     return datetime.fromisoformat(iso_str)

# parse_iso_date("2023-07-06T12:34:56")

"""
### Assignment 2: `strptime`
input: "11-25-2024"
**Task:**
1. Write a function `convert_to_datetime(date_str, format_str)` 
that takes a date string and a format string (e.g., '%Y-%m-%d %H:%M:%S') 
and returns a `datetime` object.
"""
# def convert_to_datetime(date_str, format_str):
#     datetime.strptime(date_str, format_str)

# convert_to_datetime("11-25-2024", "%m-%d-%Y")

"""
### Assignment 3: `strftime`
**Task:**
1. Write a function `format_datetime(dt, format_str)` that takes a `datetime` object and a format string (e.g., '%Y-%m-%d %H:%M:%S') and returns a formatted string.
2. output: "11/25/2024T08:20:00 PM"
"""
# def format_datetime(dt_obj, format_str):
#     dt_obj.strftime(format_str)

# dt_obj = datetime.strptime("2024-11-25 20:20:00")
# format_datetime(dt_obj, "%m/%d/%YT%I:%M:%S %p")


"""

### Assignment 4: `timedelta`
**Objective:** Understand how to perform arithmetic with datetime objects.

**Task:**
1. Write a function `calculate_future_date(start_date, days)` that takes a starting date and a number of days to add.
2. Use `timedelta` to calculate the future date.
3. Test your function with different start dates and number of days.

### Assignment 5: `replace`
**Objective:** Learn how to modify parts of a datetime object.

**Task:**
1. Write a function `modify_date(dt, year=None, month=None, day=None)` that takes a `datetime` object and optional year, month, and day parameters.
2. Use `replace` to modify the `datetime` object with the provided parameters.
3. Test your function with various datetime objects and modifications.

### Assignment 6: `today`
**Objective:** Get the current date.

**Task:**
1. Write a function `get_today_date()` that returns today's date.
2. Use `today` to implement the function.
3. Print today's date using your function.

### Assignment 7: `now`
**Objective:** Get the current date and time.

**Task:**
1. Write a function `get_current_datetime()` that returns the current date and time.
2. Use `now` to implement the function.
3. Print the current date and time using your function.

### Assignment 8: `utcnow`
**Objective:** Get the current UTC date and time.

**Task:**
1. Write a function `get_current_utc_datetime()` that returns the current UTC date and time.
2. Use `utcnow` to implement the function.
3. Print the current UTC date and time using your function.

"""
# from datetime import timedelta
# from dateutil.relativedelta import relativedelta




# dt = datetime.now()

# dd = dt - timedelta(hours=2)
# dd = dt - timedelta(minutes=2)
# dd = dt - timedelta(seconds=2)


# dt1 = date.today()
# dt2 = date.fromisoformat("1994-08-25")

# diff = dt1 - dt2
# print(diff.total_seconds())


# dtt_2 = dt - relativedelta(min=5)
# print(dtt_2)


arr = [1,2,3,4,5,6,7]
sett = {1, 2, 3, 4, 5, 6}

# O(n)
for i in arr:
    if i == 1:
        print('found')

# O(1)        
arr[4]

if 3 in arr:
    pass

if 3 in sett:
    pass


x = 100
y = 100

if x == y:
    pass

if x is y:
    pass