from functools import reduce


numbers = [3, 5, 8]
print(reduce(lambda x, y: x * y, numbers))
print("Check: ", 3 * 5 * 8)
