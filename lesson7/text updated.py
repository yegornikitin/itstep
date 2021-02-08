text = input("Please, write something: \n")
print("Number of sentences: ", len(text.split(".")))
a = [".", ",", "?", "!"]
for i in set(text):
    if i in a:
        print("Число знаков препинания: ", i, text.count(i))



