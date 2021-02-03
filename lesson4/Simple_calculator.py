while True:
    try:
        num1 = float(input('Please, enter number 1: '))
        num2 = float(input('Please, enter number 2: '))
        break
    except ValueError:
        print('Error. Enter a number')
function = input('Please, enter a function: "+", "-", "*", "/"')
if function in ('+', '-', '*', '/'):
    if function == '+':
        print(num1, "+", num2, "=", num1 + num2)
    elif function == '-':
        print(num1, "-", num2, "=", num1 - num2)
    elif function == '*':
        print(num1, "*", num2, "=", num1 * num2)
    elif function == '/':
        if num2 != 0:
            print(num1, "/", num2, "=", num1 / num2)
        else:
            print('Indivisible')
else:
    print('Not valid function')
