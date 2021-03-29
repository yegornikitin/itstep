import even_list_generate


def every_third(start, end):
    return even_list_generate.even_list_generate(start, end)[::3]


print(every_third(2, 12))
