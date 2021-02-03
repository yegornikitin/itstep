try:
    num = int(input('Enter integer number: '))
    if num >= 0:
        if num % 2 == 0:
            print(num, '=> positive even number')
        elif num % 2 != 0:
            print(num, '=> positive odd number')
    if num < 0:
        if num % 2 == 0:
            print(num, '=> negative even number')
        elif num % 2 != 0:
            print(num, ' => negative odd number')
except ValueError:
    print('Error. Enter integer number')
