Ron = {"Accio", "Wingardium Leviosa", "Alohomora"}
Harry = {"Accio", "Wingardium Leviosa", "Expelliarmus", "Expecto patronum"}

# Первое задание. Делаем функцией и методом "intersection"
def same_spells(ron_spells: set, harry_spells: set) -> set:
    same_spell = ron_spells.intersection(harry_spells)
    return same_spell

print("---------------------------")
print("1. Spells, that know both, Ron and Harry: ", same_spells(Ron, Harry))
print("---------------------------")

# Второе задание. Делаем функцией и методом "symmetric_difference"
def unique_spells(ron_spells: set, harry_spells: set) -> set:
    unique_spell = ron_spells.symmetric_difference(harry_spells)
    return unique_spell


print("2. Spells, that know only one wizard, Ron or Harry: ", unique_spells(Ron, Harry))
print("---------------------------")

# Третье задание.
def add_new_spell(spells_list: set, new_spell: str) -> bool:
    if new_spell in spells_list:
        return False
    if new_spell not in spells_list:
        new_spells_list = spells_list.add(new_spell)
        return True


print("3. Is 'Expelliarmus' new for Harry? : ", add_new_spell(Harry, "Expelliarmus"))
print("Is 'Expelliarmus' new for Ron? : ", add_new_spell(Ron, "Expelliarmus"))
print("Updated Harry spells: ", Harry)
print("Updated Ron spells: ", Ron)
print("---------------------------")

# Четвертое задание
# def add_new_spells(spells_list: set, *args: str) -> bool:

def add_new_spells(spells_list: set, *args) -> bool:
    for j in range(0, len(args)):
        for i in args:
            if i in spells_list:
                return False
                break
            else:
                new_spells_list = spells_list.add(args)
                return True


print("4. ", add_new_spells(Harry, "Expelliarmus", "Lumus", "Obliviate"))
print("Harry`s spells: ", Harry)
print("---------------------------")


# Пятое задание
def learn_all(my_spells: set, teacher_spells: set) -> set:
    new_spell = my_spells.union(teacher_spells)
    return new_spell


print("5. Spells, that Harry and Ron will know after teaching each other",
      learn_all(Harry, Ron))
