try:
    lines = input("Please, insert # of lines you want in pyramid: \n")
    # количество звезд = арифметическая прогрессия
    # первое число = 1, шаг = 2
    if type(int(lines)) == int:
        final_number = 1 + ((int(lines) - 1) * 2)
        for i in reversed(range(0, final_number)):
            print(" " * i + "*" * (final_number - i * 2) + " " * i)
except ValueError:
    print("Error, please rewrite number")
