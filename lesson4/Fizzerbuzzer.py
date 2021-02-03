error = "Please, enter a number in a range from 1 to 100"
try:
    number = float(input('Enter a number in range from 1 to 100: '))
    if 100 >= number >= 1:
        if number % 3 == 0 and number % 5 == 0:
            print('FizzBuzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
    else:
        print(error)
except ValueError:
    print(error)
