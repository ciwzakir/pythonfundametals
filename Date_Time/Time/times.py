import time

seconds = time.time()
print("Current time in seconds:", seconds)

local_time = time.localtime(seconds)
print('Local Time', local_time)

# time in string form
print('Time in String:', time.ctime(seconds))

# Formatting the time to display in string format
print('Formatted Time:', time.strftime("%d/%m/%Y %H:%M:%S", local_time))

# String to Time Object
print('Time object:', time.strptime("16/07/2021 17:33:37", "%d/%m/%Y %H:%M:%S"))