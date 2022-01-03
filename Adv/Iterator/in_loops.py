player_list = ["Tamim","Sumya Sarkar","Mosfiqur Rahim",'Liton Das']

iterable_objects = iter(player_list)

# in while loop
while(True):
    try:
        element = next(iterable_objects)
        print(element)

    except:
        StopIteration
        break



# in for loop
print("G=======================A========================P")

for batter in player_list:
    print(batter)