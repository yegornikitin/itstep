def line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        a = symbol * length
        print(a.replace("", "\n"))
    else:
        print("Error")


line(5, "horizontal", "&")
