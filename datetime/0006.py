import datetime 

current_date_time = datetime.datetime.now()

current_date = current_date_time.strftime("%x")
current_time = current_date_time.strftime("%X")

print("current date:", current_date)
print("current time:", current_time)

"""
current date: 02/19/21
current time: 11:27:57
"""
