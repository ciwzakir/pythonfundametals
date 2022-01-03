from datetime import datetime, date, time, timedelta

# Time delta is the defference of two date
# 

today_is = datetime.today()
dob = "07/01/1990"
convert_dob = datetime.strptime(dob, "%d/%m/%Y")

age_is = today_is - convert_dob
print(convert_dob)
print(type(age_is))
print("Age is ", age_is)
