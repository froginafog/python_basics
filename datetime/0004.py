import datetime 

year = 2021
month = 5
day = 20
hour = 11
minute = 30
second = 45

my_date_time = datetime.datetime(year, month, day, hour, minute, second)

my_date_time = my_date_time.strftime("%c")

print(my_date_time)

"""
Thu May 20 11:30:45 2021
"""
