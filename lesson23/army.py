class Army:
    def __init__(self, amount, damage, health):
        self.amount = amount
        self.damage = damage
        self.health = health

    def __str__(self):
        return f"{self.amount}, {self.damage}, {self.health}"

    def __add__(self, other):
        return Army(self.amount + other.amount,
                       (self.damage*self.amount + other.damage*other.amount)/(self.amount + other.amount),
                       (self.health*self.amount + other.health*other.amount)/(self.amount + other.amount))

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return Army(self.amount - other.amount, self.damage, self.health)
        else:
            return Army(0, self.damage, self.health)


class OrkArmy(Army):
    def receive_damage(self, damage: int):
        died_orks = (self.amount * self.health / damage)
        if self.amount > died_orks:
            self.amount = self.amount - died_orks
            return (died_orks)
        else:
            return (self.amount)


class ElfArmy(Army):
    def __init__(self, amount, damage, health, shield):
        Army.__init__(self, amount, damage, health)
        self.shield = shield

    def receive_damage(self, damage: int):
        died_elfs = ((self.amount * (self.health + self.shield)) / damage)
        if self.amount > died_elfs:
            self.amount = self.amount - died_elfs
            return (died_elfs)
        else:
            return (self.amount)

#
# if __name__ == "__main__":
#     first_elf_army = ElfArmy(1000, 100, 100, 30)
#     print(first_elf_army.receive_damage(5000))
#     first_army = OrkArmy(500, 100, 100)
#     second_army = OrkArmy(500, 50, 50)
#     print(first_army + second_army)
#     print(first_army - second_army)
#     print(first_army.receive_damage(3000))
