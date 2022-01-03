from datetime import datetime, date, timedelta


"""
print(dir(datetime))
date Class
time Class
datetime Class
timedelta Class

"""
today = date.today()
# print('Today:', today)

# # extract attributes
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)
# Date String in dd/mm/yyyy HH:MM:SS format
dt_string1 = "12/06/2021 09:15:32"

# strptime used to Convert string to datetime object
# Same formate is to be used as in the string
dt_object1 = datetime.strptime(dt_string1, "%d/%m/%Y %H:%M:%S")
uuggy = today - dt_object1
print(dt_object1)
# print(uuggy)
