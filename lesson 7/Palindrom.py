user_input = input("Please, write something: \n")
try:
    for i in range(0, len(str(user_input))):
        if str(user_input)[i] != str(user_input)[-1 - i]:
            print("It's not a palindrome")
            break
    else:
        print("It's palindrome")
except ValueError:
    print("Error")
