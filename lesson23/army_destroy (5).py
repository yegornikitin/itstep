from army import Army
from army import OrkArmy
from army import ElfArmy

class GnomeArmy(Army):
    def receive_damage(self, damage: int):
        died_gnomes = (self.amount * self.health / damage)
        if self.amount > died_gnomes:
            self.amount = self.amount - died_gnomes
            return (died_gnomes)
        else:
            return (self.amount)


ork_army_1 = OrkArmy(500, 100, 100)
elf_army_1 = ElfArmy(700, 90, 90, 10)
gnome_army_1 = GnomeArmy(400, 110, 110)
list_of_armies = [ork_army_1, elf_army_1, gnome_army_1]


def damage_of_army():
    num_of_dam = int(input("Please, insert a number of damage: "))
    print("Died orks", ork_army_1.receive_damage(num_of_dam), "Remaining amount of orks: ", ork_army_1.amount)
    print("Died elfs", elf_army_1.receive_damage(num_of_dam), "Remaining amount of elfs: ", elf_army_1.amount)
    print("Died gnomes", gnome_army_1.receive_damage(num_of_dam), "Remaining amount of gnomes: ", gnome_army_1.amount)


try:
    if __name__ == "__main__":
        damage_of_army()
except:
    input("Not correct input")
