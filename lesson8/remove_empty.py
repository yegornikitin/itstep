list_with_strings = ["My name", " ", "is Yegor", " ", "My surname", " ", "is Nikitin"]
print(list_with_strings)
for el in list_with_strings:
    if el == " ":
        list_with_strings.remove(" ")
print(list_with_strings)
