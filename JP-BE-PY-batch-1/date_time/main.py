# date manipulation

import pytz


# all_tz = pytz.all_timezones
# current_dt = datetime.now(tz=pytz.timezone("Asia/Karachi"))
# print(current_dt)


# dt_str = "2023-08-15 15:50:00" # US/Pacific
# dt_obj = datetime.fromisoformat(dt_str)
# print(dt_obj)

# dt_obj = dt_obj.replace(tzinfo=pytz.timezone("Asia/Karachi"))
# print(dt_obj)


tz_detail = pytz.timezone("US/Pacific")
dt_str = "2020-03-07 15:00:00"  # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)

tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt)


print(tz_aware_dt.replace(day=9))

print(tz_aware_dt + timedelta(days=2))


tz_detail = pytz.timezone("US/Pacific")
dt_str = "2020-03-09 15:00:00"  # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)

tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt)

#
tz_aware_dt.astimezone(pytz.timezone(""))
