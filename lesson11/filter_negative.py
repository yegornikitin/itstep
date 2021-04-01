numbers = [-10, 9, -8, 7, 6, -5, -4, 3, 2, -1, 0]

def filter_negative(number):
    negative_number = range(-100000, 0)

    if number in negative_number:
        return True
    else:
        return False



filtered_negative = filter(filter_negative, numbers)
print("Negative numbers are:")

for negative_number in filtered_negative:
    print(negative_number)
