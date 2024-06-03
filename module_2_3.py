my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

count = 0

while count < len(my_list):
    print(my_list[count])
    count += 1
    if my_list[count] >= 0:
        continue
    elif my_list[count] == 0:
        del my_list[count]
    elif my_list[count] < 0:
        break
