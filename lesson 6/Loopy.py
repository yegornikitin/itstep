numbers_list = list(range(1, 100))
for i in reversed(numbers_list):
    if i < 10:
        print(i)
    elif i > 10:
        if i % 11 == 0:
            print(i)
