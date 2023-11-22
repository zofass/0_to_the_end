first_list = [0,20,35,21,0,52,0,54,3,0]
second_list = [x for x in first_list if x != 0]
zeros = len(first_list) - len(second_list)
second_list.extend( [0] * zeros)
print(second_list)