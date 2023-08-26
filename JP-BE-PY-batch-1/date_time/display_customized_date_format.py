
# display customized date format
from datetime import datetime, date

print("display customized date format")
date_iso = datetime.now()
print("iso_formatted_date:", date_iso)

pak_formatted_date = datetime.strftime(date_iso, "%d-%m-%Y")
print("pak formatted date:", pak_formatted_date)

us_formatted_date = datetime.strftime(date_iso, "%m/%d/%Y")
print("US formatted date:", us_formatted_date)

date_formatted_12_hour = datetime.strftime(date_iso, "%d-%m-%Y %I:%M:%S %p")
print("display date in 12 hours format:", date_formatted_12_hour)

date_formatted_24_hour = datetime.strftime(date_iso, "%Y-%m-d %H:%M:%S")
print("display date in 24 hours format:", date_formatted_24_hour)

date_formatted_with_weekday_name = datetime.strftime(date_iso, "%Y-%m-d %H:%M:%S %A")
print("display date in 24 hours format:", date_formatted_with_weekday_name)


# https://strftime.org/
