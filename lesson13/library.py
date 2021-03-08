# Список идентификационных кодов
year_lst = ["1981", "2013", "2001", "1983", "1986"]
# Список телефонных номеров (индекс каждого номера соответствует ИНН)
book_lst = ["Cujo", "Joyland", "Dreamcatcher", "Pet Sematary", "Misery"]
# Алфавит (для сортировки по названию)
alphabet = ["a", "b", "C", "D", "e", "f", "g", "h", "I", "J", "k", "l",
            "M", "n", "o", "P", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# Обращение к юзеру. Меньюал, что делает программа
print("---------------\n"
      "This is the library of Stephen King books. "
      "You can sort the library by: \n"
      "1. The year of the books \n"
      "2. The name of the books \n"
      "Also you can request full list of books or exit the program.\n"
      "---------------")
try:
    # Инпут юзера
    user_input = input("What do you want to try? Please, enter: \n"
                       "'year' - to sort down by year of the books, \n"
                       "'names' - to sort down by the names of the books, \n"
                       "'full list' - to see full list of books, \n"
                       "'exit' - to stop the program \n"
                       "---------------\n"
                       "Your choice: ")

    # 1. Выдача полного списка
    if user_input == "full list":
        def full_list(year_lst, book_lst):
            len_year_list = len(year_lst)
            len_book_list = len(book_lst)
            full_lst = []
            for i in range(0, len_year_list):
                for j in range(0, len_book_list):
                    if i == j:
                        full = book_lst[j] + ", " + year_lst[i]
                        full_lst.append(full)
                    else:
                        continue
            print('\n'.join(full_lst))


        full_list(year_lst, book_lst)

    # 2. Сортировка по году выпуска (включая названия книг)
    elif user_input == "year":
        def inn_sort(year_lst):
            len_year_list = len(year_lst)
            len_book_list = len(book_lst)
            sorted_lst = []
            #  Сортируем методом больбашки года + если меняются местами года, то меняются и названия
            for inn in range(0, len_year_list):
                for tel in range(0, len_book_list):
                    for i in range(0, len_year_list - 1):
                        for j in range(0, len_book_list - 1):
                            if i == j:
                                if year_lst[i] > year_lst[i + 1]:
                                    year_lst[i], year_lst[i + 1] = year_lst[i + 1], year_lst[i]
                                    book_lst[j], book_lst[j + 1] = book_lst[j + 1], book_lst[j]
            #  Вывод отсортированных данных : отсортированные года + их названия
            for i in range(0, len_year_list):
                for j in range(0, len_book_list):
                    if i == j:
                        full = year_lst[i] + ", " + book_lst[j]
                        sorted_lst.append(full)
                    else:
                        continue
            print('\n'.join(sorted_lst))


        inn_sort(year_lst)


    # 3. Сортировка по названию книг (включая года)
    elif user_input == "names":
        def names_sort(book_lst):
            # Определение индекса первой буквы названия в алфавите и введение каждого индекса в отдельный список
            index_list = []
            for book in book_lst:
                index = 0
                for letter in alphabet:
                    if book[0] != letter:
                        index += 1
                        continue
                    else:
                        index_list.append(index)
                        index += 1
                        break
                    continue
            # Сортировка методом пузыря
            len_year_list = len(year_lst)
            len_book_list = len(book_lst)
            sorted_lst = []
            for book in range(0, len_book_list - 1):
                for year in range(0, len_year_list - 1):
                    for i in range(0, len(index_list)):
                        if book == i:
                            if book == year:
                                if index_list[i] > index_list[i + 1]:
                                    book_lst[i], book_lst[i + 1] = book_lst[i + 1], book_lst[i]
                                    year_lst[i], year_lst[i + 1] = year_lst[i + 1], year_lst[i]
            #  Вывод отсортированных данных : отсортированные названия + их года
            for i in range(0, len_year_list):
                for j in range(0, len_book_list):
                    if i == j:
                        full = book_lst[j] + ", " + year_lst[i]
                        sorted_lst.append(full)
                    else:
                        continue
            print('\n'.join(sorted_lst))


        names_sort(book_lst)

    # 4. Выход из программы
    elif user_input == "exit":
        exit

    # Ошибка, если некорректный инпут
    else:
        print("Error. Not correct choice. Try one more time")

except ValueError:
    print("Error. Not correct choice. Try one more time")
