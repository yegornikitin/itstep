try:
    num1 = float(input('Please, enter the first number: '))
    num2 = float(input('Please, enter the second number: '))
    if num1 == num2:
        print('The numbers are equal')
    elif num1 > num2:
        print("Not equal; \nThe bigger number is: ", num1)
        print("The lower number is: ", num2)
    else:
        print("Not equal; \nThe bigger number is: ", num2)
        print("The lower number is: ", num1)
except ValueError:
    print('Am I a Joke to you?')
