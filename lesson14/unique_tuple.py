def unique(tupl1:tuple, tupl2:tuple,tupl3:tuple):
    list_unique = []
    for i in tupl1:
        if i not in tupl2:
            if i not in tupl3:
                list_unique.append(i)
    for j in tupl2:
        if j not in tupl1:
            if j not in tupl3:
                list_unique.append(j)
    for k in tupl3:
        if k not in tupl1:
            if k not in tupl2:
                list_unique.append(k)

    tpl_unique = tuple(list_unique)
    print("Result tuple: ", tpl_unique)


unique((4, 2, 6, 7), (1, 2, 7, 2, 9), (2, 2, 2, 7, 1))

