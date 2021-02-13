user_input = input("Please, write your text (sentences divide with'. '): \n")
split_user_input = user_input.split(". ")
for i in split_user_input:
    print(i.capitalize(), end=". ")
