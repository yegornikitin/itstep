numbers_list = list(range(1, 10))
user_inp = input("Please, enter a number from 1 to 10: \n")
error = "Please, enter correct number (1 - 10)"
for i in numbers_list:
    try:
        if type(int(user_inp)) == int:
            if 0 < int(user_inp) < 11:
                print(user_inp, "*", i, "=", int(user_inp) * i)
            else:
                print(error)
                break
    except ValueError:
        if type(user_inp) == str:
            print(error)
            break
