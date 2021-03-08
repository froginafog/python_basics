import datetime 

current_date_time = datetime.datetime.now()

current_hour = current_date_time.strftime("%l") #hour in 00-12 format
current_minute = current_date_time.strftime("%M") #minute in 00-59 format
current_second = current_date_time.strftime("%S") #second in 00-59 format 
am_pm = current_date_time.strftime("%p")

print("current time: " + current_hour + ":" + current_minute + ":" + current_second + " " + am_pm)

"""
current time: 11:34:48 AM
"""
