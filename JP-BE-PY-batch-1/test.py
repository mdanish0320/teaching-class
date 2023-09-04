import pytz
from datetime import datetime, timedelta

# def get_tz_from_country_code(country_code):
#     for _country_code, tz in pytz.country_timezones.items():
# 	    if country_code == _country_code:
#                 return tz

# def get_country_code(country_name):
#     for code, name in pytz.country_names.items():
#         print(code, "-", name)
#         if name.lower().find(country_name) > -1:
#                 return code

# def get_country_tz(country_name):
#     print("country_name", country_name)
#     country_code = get_country_code(country_name.lower())
#     print(country_code)
#     return get_tz_from_country_code(country_code)

# tz = get_country_tz("united stat")
# print(tz)





# str_dt = "2023-08-01 18:00:00" # local time of Pacific
# pacific_dt = datetime.fromisoformat(str_dt)
# pacific_tz = pytz.timezone("US/Pacific")
# pacific_local_datetime = pacific_tz.localize(pacific_dt)
# print(pacific_local_datetime)


"""
In the Pacific Time Zone (US/Pacific), which includes cities like Los Angeles, San Francisco, and Seattle, the Daylight Saving Time (DST) changes for the year 2020 were as follows:

DST Start (Spring Forward):

Start Date: March 8, 2020
Time: Clocks were moved forward by 1 hour at 2:00 AM local time, becoming 3:00 AM.
DST End (Fall Back):

End Date: November 1, 2020
Time: Clocks were moved backward by 1 hour at 2:00 AM local time, becoming 1:00 AM.
"""

dt = "2020-03-07 15:00:00" # US/Pacific
dt = datetime.fromisoformat(dt)
print(dt_tz.localize(dt))

print(dt_tz.localize(dt) + timedelta(hours=5))

print("")

dt = "2020-03-08 15:00:00" # US/Pacific
dt = datetime.fromisoformat(dt)
dt_tz = pytz.timezone("US/Pacific")
print(dt_tz.localize(dt))
dt_tz = pytz.timezone("US/Pacific")