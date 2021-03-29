from random import randint


def recursive_func(numbers: list, start: int, minimum: int):
    if start == len(numbers) - 10:
        return minimum
    else:
        if sum(numbers[start:start + 10]) < sum(numbers[minimum:minimum + 10]):
            minimum = start
        return recursive_func(numbers, start + 1, minimum)


list_of_numbers = []
for i in range(0, 100):
    values = randint(0, 100)
    list_of_numbers.append(values)

print("Len of random list: ", len(list_of_numbers))
print("Random list: ", list_of_numbers)
print("-------------")
print("Normal range (0,100) result: ", recursive_func(list(range(0, 100)), 0, 0))
print("Result position on random list generated: ", recursive_func(list_of_numbers, 0, 0))
print("Result sum on random list generated: ", sum(list_of_numbers[recursive_func(list_of_numbers, 0, 0):recursive_func(list_of_numbers, 0, 0)+10]))
