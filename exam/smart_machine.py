try:
    user_input = int(input("Please, enter a number: \n"))
    if user_input < 100:
        print("Output: ", user_input - 10)
    else:
        print("Output: ", user_input - 20)
except ValueError:
    print("Error. Please, enter a number")
