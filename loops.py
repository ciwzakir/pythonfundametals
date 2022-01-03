
tuple = (11,12,13,14,14,14) # Duplicate allowed
player_list = ["Mosfiqur Rahim", "Tamim", 'Liton Das', "Sumya Sarkar"]
diner_sets = {"Plates", "Half Plates", 'Rice Serving Dish', "Tea Cup", "Curry Bowl"} 
dictionery = {"Come": "আসা", "Go":"যাওয়া", "eat":"খাওয়া", "understand":"বুঝতে পারা"} 

# There are two types of loops in python For loop and while loop

"""
for loops are executed a fixed number of times
for loop runs till it reaches the last element in the sequence. If it reaches the last element in the sequence,
it exits the loop. otherwise, it keeps on executing the statements

"""
for data in tuple:
    print(data)

for playing_today in player_list:
    print(playing_today)

for item in diner_sets:
    print(item)

for word in dictionery:
    print(word ," meaning is ", dictionery[word])

#   while loop executes/runs a set of statement as long as the condition is true then it stops
#   An unknown number of times

cash_in_hand = 10 # initialise value is 10

while cash_in_hand >=1:
    print(cash_in_hand) # Spend your money by 1 as long as your cash in hand greater than or equal to 1
    cash_in_hand -= 1 # decreasing rate is 1
