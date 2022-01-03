from datetime import datetime, time


# Extract time from datetime object
now = datetime.now()
print("Current time is:", now.time())

# Create empty time object
t = time()
print('Time', t)

# create time object with attribute names
t1 = time(hour=7, minute=10, second=34)
print("time is:", t1)

# time without attributes names
t2 = time(7, 10, 45)
print("time is:", t2)

# time with microseconds
t3 = time(7, 10, 45, 400437)
print("time is:", t3)