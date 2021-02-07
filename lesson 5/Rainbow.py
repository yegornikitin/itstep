colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
error = "Please, write the colour with a capital letter"
try:
    user_input = input("Please, write one of the Rainbow colours with the capital letter: \n")
    if user_input in colours:
        user_input_index = colours.index(user_input)
        if user_input_index == 0:
            print("The next colour is:", colours[user_input_index+1],
                  ", and no previous colours.")
        elif user_input_index == 6:
            print("The previous colour is:", colours[user_input_index-1],
                  ", and no next colours.")
        elif 0 < user_input_index < 6:
            print("The previous colour is:", colours[user_input_index-1],
                  "and the next colour is:", colours[user_input_index+1])
    else:
        print(error)
except ValueError:
    print(error)
