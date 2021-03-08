from datetime import datetime

print("datetime.now()            :", datetime.now())
print("datetime.now().year       :", datetime.now().year)
print("datetime.now().month      :", datetime.now().month)
print("datetime.now().day        :", datetime.now().day)
print("datetime.now().hour       :", datetime.now().hour)
print("datetime.now().minute     :", datetime.now().minute)
print("datetime.now().second     :", datetime.now().second)
print("datetime.now().microsecond:", datetime.now().microsecond)
print(dir(datetime.now()))

"""
datetime.now()            : 2020-12-13 19:43:08.477367
datetime.now().year       : 2020
datetime.now().month      : 12
datetime.now().day        : 13
datetime.now().hour       : 19
datetime.now().minute     : 43
datetime.now().second     : 8
datetime.now().microsecond: 512724
"""
