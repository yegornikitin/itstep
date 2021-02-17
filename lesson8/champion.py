number_of_set = 1
user_stop = "stop"
list_of_repetitions = []
while True:
    user_input = input(f"Введите количество повторений в подходе №{number_of_set}"
                       f", или 'stop', чтобы подсчитать результаты: ")
    try:
        repetitions = int(user_input)
        if repetitions < 0:
            print("Введите целое положительное число или 'stop'. ")
        else:
            number_of_set += 1
            list_of_repetitions.append(repetitions)
    except ValueError:
        if user_input == user_stop:
            print(f'Количество подходов: {number_of_set - 1}')
            print(f'Общее количество повторений: {sum(list_of_repetitions)}')
            print(f'Максимальное количество повторений: {max(list_of_repetitions)}')
            print(f'Минимальное количество повторений: {min(list_of_repetitions)}')
            print(f'Среднее количество повторений за подход {sum(list_of_repetitions) / len(list_of_repetitions)}')
            break
        else:
            print("Введите целое положительное число или 'stop'.")
