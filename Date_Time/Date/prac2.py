from datetime import *
# strftime is used for date time formating
# strftime is used for date time formating
today_ = date.today()
today1_ = datetime.today()
print(today_)
print(today1_)

now_ = datetime.now()
print(now_)

obj1_of_now_ = datetime.strftime(now_, "%d %b %y")
print(obj1_of_now_)

obj2_of_now_ = datetime.strftime(now_, "%d %B %Y")
print(obj2_of_now_)

obj3_of_now_ = datetime.strftime(now_, "%d %B %Y %H:%M:%S")
print(obj3_of_now_)

# %p for AM PM and %f for microseconds

obj3_of_now_ = datetime.strftime(now_, "%d %B %Y %I:%M:%S:%f, %p")
print(obj3_of_now_)
