def only_odd_arguments(func):
    def wrapper(*args):
        i = 1
        n = len(args)
        for element in args:
            if i < n:
                # Проверка всех элементов списка, не включая последний элемент
                if element % 2 == 0:
                    print("Error. Please, add odd numbers!")
                    i += 1
                    break
                else:
                    i += 1
                    continue
            else:
                # Проверка последнего элемента списка
                if element % 2 == 0:
                    print("Error. Please, add odd numbers!")
                    i += 1
                    break
                else:
                    print(func(*args))
                    break

    return wrapper


@only_odd_arguments
def add(a, b):
    return a + b


print("Add results:")
add(4, 4)
add(4, 5)
add(5, 5)

print("------------")


@only_odd_arguments
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print("multiply results:")
multiply(4, 5, 7, 9, 3)
multiply(1, 5, 7, 9, 3)
