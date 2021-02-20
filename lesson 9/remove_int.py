def remove_int(values_list, num):
    while num in values_list:
        values_list == values_list.remove(num)
        new_values_list = values_list.copy()
    print(new_values_list)


remove_int([4, 3, 4, 5, 4, 7, 6], 4)
