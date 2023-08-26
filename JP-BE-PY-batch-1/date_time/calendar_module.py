# get last day of the month
import calendar

month_r = calendar.monthrange(
    2023, 1
)
print("last day of the month jan 2023 is:", month_r[1])

month_r = calendar.monthrange(
    2023, 2
)
print("last day of the month feb 2023 is:", month_r[1])


month_r = calendar.monthrange(
    2023, 3
)
print("last day of the month mar 2023 is:", month_r[1])

month_r = calendar.monthrange(
    2023, 4
)
print("last day of the month apr 2023 is:", month_r[1])
