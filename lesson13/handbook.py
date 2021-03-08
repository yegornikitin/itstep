# Список идентификационных кодов
inn_lst = ["374659", "357863", "890087", "112837", "789457"]
# Список телефонных номеров (индекс каждого номера соответствует ИНН)
tel_lst = ["067-784-07-76", "098-876-90-07", "050-075-76-65", "095-768-57-68", "093-435-00-00"]
# Обращение к юзеру. Меньюал, что делает программа
print("This is the handbook, that contains: 1. INNs of the users; 2. Telephone numbers of the users. "
      "You can sort the handbook, or exit the program.")
try:
    # Инпут юзера
    user_input = input("What do you want to sort? Please, enter: \n"
                       "'inn' - to sort down by INNs, \n"
                       "'numbers' - to sort down by telephone numbers, \n"
                       "'full list' - to see full list of users, \n"
                       "'exit' - to stop the program \n"
                       "Your choice: ")

    # 1. Выдача полного списка
    if user_input == "full list":
        def full_list(inn_lst, tel_lst):
            len_inn_list = len(inn_lst)
            len_tel_list = len(tel_lst)
            full_lst = []
            for i in range(0, len_inn_list):
                for j in range(0, len_tel_list):
                    if i == j:
                        full = "INN: " + inn_lst[i] + "; Tel: " + tel_lst[j]
                        full_lst.append(full)
                    else:
                        continue
            print(full_lst)


        full_list(inn_lst, tel_lst)

    # 2. Сортировка по ИНН (включая номера телефонов)
    elif user_input == "inn":
        def inn_sort(inn_lst):
            len_inn_list = len(inn_lst)
            len_tel_list = len(tel_lst)
            sorted_lst = []
            #  Сортируем методом больбашки ИНН + если меняются местами ИНН, то меняются и телефоны
            for inn in range(0, len_inn_list):
                for tel in range(0, len_tel_list):
                    for i in range(0, len_inn_list - 1):
                        for j in range(0, len_tel_list - 1):
                            if i == j:
                                if inn_lst[i] > inn_lst[i + 1]:
                                    inn_lst[i], inn_lst[i + 1] = inn_lst[i + 1], inn_lst[i]
                                    tel_lst[j], tel_lst[j + 1] = tel_lst[j + 1], tel_lst[j]
            #  Вывод отсортированных данных : отсортированные ИНН + их телефоны
            for i in range(0, len_inn_list):
                for j in range(0, len_tel_list):
                    if i == j:
                        full = "INN: " + inn_lst[i] + "; Tel: " + tel_lst[j]
                        sorted_lst.append(full)
                    else:
                        continue
            print(sorted_lst)


        inn_sort(inn_lst)


    # 3. Сортировка по номеру телефона (включая ИНН)
    elif user_input == "numbers":
        def numbers_sort(tel_lst):
            len_inn_list = len(inn_lst)
            len_tel_list = len(tel_lst)
            sorted_lst = []
            #  Сортируем методом больбашки Телефоны + если меняются местами тел, то меняются и ИНН
            for inn in range(0, len_inn_list):
                for tel in range(0, len_tel_list):
                    for i in range(0, len_inn_list - 1):
                        for j in range(0, len_tel_list - 1):
                            if i == j:
                                if tel_lst[j] > tel_lst[j + 1]:
                                    inn_lst[i], inn_lst[i + 1] = inn_lst[i + 1], inn_lst[i]
                                    tel_lst[j], tel_lst[j + 1] = tel_lst[j + 1], tel_lst[j]
            #  Вывод отсортированных данных : отсортированные телефоны + их ИНН
            for i in range(0, len_inn_list):
                for j in range(0, len_tel_list):
                    if i == j:
                        full = "Tel: " + tel_lst[j] + "; INN: " + inn_lst[i]
                        sorted_lst.append(full)
                    else:
                        continue
            print(sorted_lst)


        numbers_sort(tel_lst)

    # 4. Выход из программы
    elif user_input == "exit":
        exit

    # Ошибка, если некорректный инпут
    else:
        print("Error. Not correct choice. Try one more time")

except ValueError:
    print("Error. Not correct choice. Try one more time")
