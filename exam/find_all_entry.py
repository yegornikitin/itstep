def find_all_entry(text, symbol):
    index = 0
    for j in text:
        if symbol != j:
            index += 1
        elif symbol == j:
            print(index)
            index += 1

text = ["n", "i", "k", "i", "t", "i", "n", "y", "e", "g", "o", "r"]
symbol = "y"


find_all_entry(text, symbol)
