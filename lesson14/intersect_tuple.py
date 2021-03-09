def intersect(tupl1:tuple, tupl2:tuple,tupl3:tuple):
    list_intersect = []
    i = 0
    for i in tupl1:
        for j in tupl2:
            for k in tupl3:
                if i == j == k:
                    list_intersect.append(i)
                    i += 1
    tpl_intersect = tuple(list_intersect)
    print("Result tuple: ", tpl_intersect)


intersect((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1))

