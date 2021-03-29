def even_list_generate(start, end):
    new_list = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            new_list.append(i)
    return new_list


if __name__ == "__main__":
    print(even_list_generate(2, 12))
