text = input("Please, write something: \n")
print(len(text.split(".")))
a = [".", ",", "?", "!"]
for i in set(text):
    if i in a:
        print(i, text.count(i))



