import datetime

# This module is used for working with time and dates
# from datetime import datetime

# mytime = datetime.time(2, 1, 3, 5)
# U can take string and parse it to datetime object
# print(mytime)
# print(mytime.microsecond)
# print(type(mytime))

# current_time = (datetime.date.today())
# print(current_time.ctime())
# my_date_time = datetime(2021, 6, 8, 6, 7, 34, 6)
# print(my_date_time)


d1 = datetime.date(2015, 3, 11)
print("d1:", d1)

d2 = d1.replace(year=1990)
print("d2:", d2)
print(d1 - d2)
