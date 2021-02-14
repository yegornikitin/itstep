a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
b = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
     "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", " "]
tex = input("Please, enter your words: \n")
new_tex = ""
count = 0
for letter in tex:
    if letter in a:
        tex = tex.replace(a[a.index(letter)], b[a.index(letter)])
        new_tex += tex[count]
        count += 1
print(new_tex)
