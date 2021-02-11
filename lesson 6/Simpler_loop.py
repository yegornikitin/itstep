i = 0
counter = 0
while True:
    if i % 5 == 0 and counter < 31:
        print(i)
        i += 5
        counter += 1
    if 0 > counter > 31:
        break