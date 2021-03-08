import datetime 

year = 2021
month = 11
day = 20
hour = 11
minute = 30
second = 45

my_date_time = datetime.datetime(year, month, day, hour, minute, second)

month_name_short = my_date_time.strftime("%b")
month_name_full = my_date_time.strftime("%B")

print(month_name_short + " " + str(day) + ", " + str(year))
print(month_name_full + " " + str(day) + ", " + str(year))

"""
Nov 20, 2021
November 20, 2021
"""
