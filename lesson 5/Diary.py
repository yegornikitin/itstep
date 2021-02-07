tasks_list = ["You have 1 task:\n 1. Read the book",
              "You fave 2 tasks:\n 1. Go to school and 2. Learn Python",
              "You fave 2 tasks:\n 1. Help Mom and 2. Do HomeWork",
              "You fave 1 task:\n 1. Take a rest",
              "You fave 2 tasks:\n 1. Learn English and 2. Read a book",
              "You have 1 task:\n 1. Clean the house",
              "You have 1 task:\n 1. Listen to music"]
tasks_voc = dict(monday="You have 1 task:\n 1. Read the book",
                 tuesday="You fave 2 tasks:\n 1. Go to school and 2. Learn Python",
                 wednesday="You fave 2 tasks:\n 1. Help Mom and 2. Do HomeWork",
                 thursday="You fave 1 task:\n 1. Take a rest",
                 friday="You fave 2 tasks:\n 1. Learn English and 2. Read a book",
                 saturday="You have 1 task:\n 1. Clean the house",
                 sunday="You have 1 task:\n 1. Listen to music")
user_input = input("Please, enter a day in one of the next format:\n "
                   "1. number format (1-7)\n "
                   "2. word format (Monday-Sunday) in any register: \n")
error = "Not appropriate format. Please, repeat"
try:
    if type(int(user_input)) == int:
        if 0 < int(user_input) < 7:
            print(tasks_list[int(user_input)-1])
        else:
            print(error)
except ValueError:
    if type(user_input) == str:
        if user_input.lower() in tasks_voc:
            print(tasks_voc[user_input.lower()])
        else:
            print(error)
    else:
        print(error)
