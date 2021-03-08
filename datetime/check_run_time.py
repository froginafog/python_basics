import datetime 

current_microseconds_start = datetime.datetime.now().microsecond

for i in range(0, 1000):
    pass
    for j in range(0, 1000):
        pass

current_microseconds_end = datetime.datetime.now().microsecond

time_elapsed_microseconds = current_microseconds_end - current_microseconds_start
time_elapsed_milliseconds = time_elapsed_microseconds / 1000
time_elapsed_seconds = time_elapsed_milliseconds / 1000
print("time taken (in microseconds) to run this program:", time_elapsed_microseconds)
print("time taken (in milliseconds) to run this program:", time_elapsed_milliseconds)
print("time taken (in seconds) to run this program     :", time_elapsed_seconds)

"""
time taken (in microseconds) to run this program: 62064
time taken (in milliseconds) to run this program: 62.064
time taken (in seconds) to run this program     : 0.062064
"""
