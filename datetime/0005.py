import datetime 

year = 2021
month = 5
day = 20
hour = 11
minute = 30
second = 45

my_date_time = datetime.datetime(year, month, day, hour, minute, second)

my_date = my_date_time.strftime("%x")
my_time = my_date_time.strftime("%X")

print(my_date)
print(my_time)

"""
05/20/21
11:30:45
"""
