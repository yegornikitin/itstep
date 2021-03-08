numbers_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def binary_search(numbers_list, input):
    left = 0
    right = len(numbers_list)
    iterations = 1
    for j in range(0, right):
        for i in range(0, right - 1):
            mid = (left + right) // 2
            print("No of iteration:", iterations, "; left.index:", left, "; mid.index:", mid,
                  "; mid.value:", numbers_list[mid], ", right.index:", right)
            if input == numbers_list[mid]:
                print("Result: Yes, in list")
                iterations += 1
                break
            elif input > numbers_list[mid]:
                left = mid
                iterations += 1
                continue
            elif input < numbers_list[mid]:
                right = mid
                iterations += 1
                continue
        break
    if input != numbers_list[mid]:
        print("Result: Input is not in list")


input = 16
binary_search(numbers_list, input)
