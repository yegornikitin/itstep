def remove_int(values_list, num):
    counter = 0
    while num in values_list:
        values_list == values_list.remove(num)
        counter += 1
    print("The number of deleted elements is: ", counter)


remove_int([4, 3, 4, 5, 4, 7, 6], 4)
