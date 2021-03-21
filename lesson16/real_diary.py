print("This is diary program.")

tasks = {"monday": ["Read the book"],
         "tuesday": ["Go to school", "Learn Python"],
         "wednesday": ["Help Mom", "Do HomeWork"],
         "thursday": ["Take a rest"],
         "friday": ["Learn English", "Read a book"],
         "saturday": ["Clean the house"],
         "sunday": ["Listen to music"]}

# Функция, которая показывает все задания на неделю
def show_week_tasks(existed_tasks: dict):
    for i in existed_tasks:
        print("Your tasks: ", i.title(), existed_tasks[i])

# Функция, которая показывает задания на день, который ввел юзер
def show_daily_tasks(existed_tasks: dict):
    day = input("Please, enter a day, tasks on which you want to see (Monday-Sunday): ")
    if day.lower() in existed_tasks:
        print("Tasks for the chosen day: ", existed_tasks[day.lower()])
    else:
        print("Not correct input")

# Функция, которая добавляет написанный юзером таск в день, выбранный юзером
def new_task(existed_tasks: dict, new_task):
    day_choice = input("Please, enter a day in which you want to add a new task: ")
    new_task = input("Your new task: ")
    for i in existed_tasks.keys():
        if i == day_choice.lower():
            if day_choice.lower() in existed_tasks:
                existed_tasks[day_choice.lower()].append(new_task)
            print("Diary is updated")
        else:
            continue


# Функция, которая удаляет выбранный юзером
def delete_task(existed_tasks: dict):
    day_choice = input("Please, enter a day in which you want to delete task: ")
    for i in existed_tasks.keys():
        if day_choice.lower() == i:
            print(existed_tasks[i])
            task_to_delete = input('Enter number of task you want to delete :\n')
            del existed_tasks[i][int(task_to_delete) - 1]
            print("Diary is updated")
        else:
            continue


try:
    while True:
        user_input = int(input("------------------------------------\n"
                               "Please, choose what you want to do: \n"
                               "Print '1' to see all tasks on the week.\n"
                               "Print '2' to see tasks for the chosen day of the week.\n"
                               "Print '3' to add new task for the chosen day.\n"
                               "Print '4' to delete chosen task from the chosen day. \n"))

        if user_input == 1:
            show_week_tasks(tasks)
            continue
        elif user_input == 2:
            show_daily_tasks(tasks)
            continue
        elif user_input == 3:
            print(new_task(tasks, new_task))
            continue
        elif user_input == 4:
            delete_task(tasks)
            continue
        else:
            print("Not correct input")

except ValueError:
    print("Not correct input. Try one more time.")
