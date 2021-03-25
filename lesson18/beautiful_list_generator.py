
def beautiful_list_generator(lst: list, marker: str, file_name: str) -> bool:
    with open(file_name, "wb") as f:
        for hero in lst:
            a = marker.encode('utf8')
            b = " ".encode('utf8')
            c = hero.encode('utf8')
            d = "\n".encode('utf8')
            f.write(a + b + c + d)
    with open(file_name, "rb") as f:
            print(f.read().decode('utf8'))


if __name__ == "__main__":
    dc_heroes = ["Batman",
                 "Superman",
                 "Flash",
                 "Green Lantern",
                 "Wonder Woman"]
    beautiful_list_generator(dc_heroes, "\u2713", "heroes.txt")






