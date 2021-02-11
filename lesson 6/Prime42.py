numbers_list = list(range(1, 1000))
counter = 0
for num in numbers_list:
    if num > 1 and counter < 42:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=", ")
            counter += 1
