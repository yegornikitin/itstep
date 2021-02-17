first_list = ["Neo", "Trinity", "Mouse"]
second_list = ["Matrix", "Forever", "Alone"]
for element in first_list:
    for el in second_list:
        print(element + " " + el, end=", ")
