user_input = input("Please, write your number \n")
try:
    if type(int(user_input)) == int:
        if int(user_input) > 1:
            for i in range(2, int(user_input)):
                if int(user_input) % i == 0:
                    print("Not a prime number")
                    break
            else:
                print("Your number is prime")
except ValueError:
    print("Error. Please, write a number")
