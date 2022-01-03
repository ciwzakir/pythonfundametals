player_list = ["Tamim","Sumya Sarkar","Mosfiqur Rahim",'Liton Das']

batting_order = iter(player_list)

opening = next(batting_order)
print(opening)

one_down = next(batting_order)
print(one_down)

two_down = next(batting_order)
print(two_down)

last_top_order = next(batting_order)
print(last_top_order)

midle_order_first_batter = next(batting_order)
print(midle_order_first_batter)
