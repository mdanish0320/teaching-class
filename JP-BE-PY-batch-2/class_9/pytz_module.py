# pip install pytz
import pytz
from datetime import datetime, timedelta

# display all the timezones in this module
print("display all the timezones in this module")
all_tz = pytz.all_timezones
print("all timezones", all_tz)
print(len(all_tz))

# create date object with timezone detail
print("\ncreate date object with timezone detail")
date_without_tz = datetime.now()
date_with_tz = datetime.now(tz=pytz.timezone("Asia/Karachi"))
print("date_without_tz", date_without_tz)
print("date_with_tz", date_with_tz)


# correct way: add timezone detail in unaware tz date object 
print("\nadd timezone detail in date object")
date_without_tz = datetime.now()
tz_detail = pytz.timezone("Asia/Karachi")
tz_aware_dt = tz_detail.localize(date_without_tz)
print("tz_aware_dt", tz_aware_dt)


# correct way: change timezone detail
print("\nchange timezone detail from KHI to Saudi Arab")
date_without_tz = datetime.now()
tz_detail = pytz.timezone("Asia/Karachi")
tz_aware_dt = tz_detail.localize(date_without_tz)
print("tz_aware_dt", tz_aware_dt)
tz_2_detail = pytz.timezone("Asia/Riyadh")
print("updated_tz_detail", tz_aware_dt.astimezone(tz_2_detail))


# parse date string with timezone detail
print("\nparse date string with timezone detail")
saudi_arab_dt_str = "2023-08-26 15:18:33.983780+03:00"
saudi_arab_dt_obj = datetime.strptime(saudi_arab_dt_str, "%Y-%m-%d %H:%M:%S.%f%z")
print(saudi_arab_dt_obj.tzinfo)



# wrong way of adding timezone detail
dt_str = "2023-08-15 15:50:00" # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)
dt_obj = dt_obj.replace(tzinfo=pytz.timezone("Asia/Karachi"))


# wrong way of updating timezone detail
dt_obj = datetime.utcnow() # timezone 00:00
dt_obj_tz_aware = dt_obj.astimezone(pytz.timezone("Asia/Riyadh")) # this will assume UTC date as localtime
print("utcnow converted to tz aware date object")
print(dt_obj) # UTC
print(dt_obj_tz_aware) # wrong tz converted hour. it should add 3 hours in utc date and not subtract 2 hours


# changing date using replace/timedelta will not aware of the changing DST
print("\nchanging date using replace/timedelta will not aware of the changing DST")
tz_detail = pytz.timezone("US/Pacific")
dt_str = "2020-03-07 15:00:00"  # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)
tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt, "before DST Activation")


print(tz_aware_dt.replace(day=9), "DST Activated on this day but our date obj doesn't know")
print(tz_aware_dt + timedelta(days=2), "DST Activated on this day but our date obj doesn't know")


tz_detail = pytz.timezone("US/Pacific")
dt_str = "2020-03-09 15:00:00"  # US/Pacific
dt_obj = datetime.fromisoformat(dt_str)
tz_aware_dt = tz_detail.localize(dt_obj)
print(tz_aware_dt, "DST Activated on this day and date obj is aware")

## convert current time to another timezone
# what time is it in Riyadh?
datetime.now(pytz.timezone("Asia/Riyadh")) # datetime.datetime(2023, 10, 2, 16, 45, 17, 682475, tzinfo=<DstTzInfo 'Asia/Riyadh' +03+3:00:00 STD>)
