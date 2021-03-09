def same_pos(tupl1:tuple, tupl2:tuple,tupl3:tuple):
    len1 = len(tupl1)
    len2 = len(tupl2)
    len3 = len(tupl3)
    new_dict = {}
    for i in range(0, len1):
        for j in range(0, len2):
            for k in range(0, len3):
                if tupl1[i] == tupl2[j] == tupl3[k]:
                    new_dict[tupl1[i]] = i
                    break
    print("Result dict: ", new_dict)


same_pos((4, 2, 6, 7), (1, 2, 7, 7), (2, 2, 2, 7, 1))
