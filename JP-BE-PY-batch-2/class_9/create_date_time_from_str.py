# create date and time from string
from datetime import datetime, date


print("create date and time with ISO formatted string date")
date_iso = "2023-08-26"  # ISO 8601
dt_obj = date.fromisoformat(date_iso)
print(dt_obj.year)

datetime_iso = "2023-08-26 20:50:45"  # ISO 8601
dt_obj = datetime.fromisoformat(datetime_iso)
print(dt_obj.year)


# https://strftime.org/
# create date object from string other than is ISO
print("\ncreate date object from string other than ISO")
dt_pakistan_format = "26-08-2023"
dt_united_states_format = "08/26/2023"
dt_iso_format = "2023-08-26"
invalid_dt = "2023/-08--/26"
dt_12_hour_format = "26-08-2023 08:10:00 PM"
dt_named_and_short_form_format = "8-September-23 08:10:00"

dt = datetime.strptime(
    dt_pakistan_format,
    "%d-%m-%Y"
)
print("date obj converted from pak date format:", dt)


dt = datetime.strptime(
    dt_united_states_format,
    "%m/%d/%Y"
)
print("date obj converted from united state date format:", dt)


dt = datetime.strptime(
    dt_iso_format,
    "%Y-%m-%d"
)
print("date obj converted from iso date format:", dt)


dt = datetime.strptime(
    invalid_dt,
    "%Y/-%m--/%d"
)
print("date obj converted from invalid date format:", dt)

dt = datetime.strptime(
    dt_12_hour_format,
    "%d-%m-%Y %I:%M:%S %p"
)
print("date obj converted from 12 hour format:", dt)

dt = datetime.strptime(
    dt_named_and_short_form_format,
    "%d-%B-%y %H:%M:%S"
)
print("date obj converted from dt_named_and_short_form_format:", dt)



# create datetime from ISO date string that is timezone aware
print("create date from tz aware date string")
datetime_iso = "2023-08-26 20:50:45+05:00"  # ISO 8601
dt_obj = datetime.fromisoformat(datetime_iso)
print(dt_obj.year)
print(dt_obj.tzinfo)


# create datetime from NON-ISO date string that is timezone aware
datetime_non_iso = "2023/08/26 20:50:45+05:00"  # non ISO
dt_obj = datetime.strptime(datetime_non_iso, "%Y/%m/%d %H:%M:%S%z")
print(dt_obj.year)
print(dt_obj.tzinfo)

# datetiem containd microseconds
datetime.strptime(
    "2023-01-01 23:59:59.123+02:00",
    "%Y-%m-%d %H:%M:%S.%f%z"
)

print(dt.year)

