
def bubble_sort(num_list, reverse=False):
    len_list = len(num_list)
    for j in range(0, len_list):
        for i in range(0, len_list-1):
            if reverse == False:
                if num_list[i] > num_list[i+1]:
                    num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
            else:
                if num_list[i] < num_list[i+1]:
                    num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
    print("New list is: ", num_list)


bubble_sort([3, 5, 6, 4, 7, 1, 0], True)

