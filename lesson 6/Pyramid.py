lines = 15
# количество звезд = арифметическая прогрессия
# первое число = 1, шаг = 2
final_number = 1 + ((lines - 1) * 2)
for i in reversed(range(0, final_number)):
    print(' ' * i + '*' * (final_number - i * 2) + ' ' * i)
