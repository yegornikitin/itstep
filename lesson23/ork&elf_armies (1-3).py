class OrkArmy:
    def __init__(self, amount, damage, health):
        self.amount = amount
        self.damage = damage
        self.health = health

    def __str__(self):
        return f"{self.amount}, {self.damage}, {self.health}"


    def __add__(self, other):
        return OrkArmy(self.amount + other.amount,
                       (self.damage*self.amount + other.damage*other.amount)/(self.amount + other.amount),
                       (self.health*self.amount + other.health*other.amount)/(self.amount + other.amount))

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return OrkArmy(self.amount - other.amount, self.damage, self.health)
        else:
            return OrkArmy(0, self.damage, self.health)

    def receive_damage(self, damage: int):
        died_orks = (self.amount * self.health / damage)
        if self.amount > died_orks:
            self.amount = self.amount - died_orks
            return (died_orks)
        else:
            return (self.amount)


# if __name__ == "__main__":
    # first_army = OrkArmy(500, 100, 100)
    # second_army = OrkArmy(500, 50, 50)
    # print(first_army + second_army)
    # print(first_army - second_army)
    # first_army = OrkArmy(500, 100, 100)
    # print(first_army.receive_damage(3000))


class ElfArmy:
    def __init__(self, amount, damage, health, shield):
        self.amount = amount
        self.damage = damage
        self.health = health
        self.shield = shield

    def __str__(self):
        return f"{self.amount}, {self.damage}, {self.health}, {self.shield}"


    def __add__(self, other):
        return ElfArmy(self.amount + other.amount,
                       (self.damage*self.amount + other.damage*other.amount)/(self.amount + other.amount),
                       (self.health*self.amount + other.health*other.amount)/(self.amount + other.amount),
                       (self.shield*self.amount + other.shield*other.amount)/(self.amount + other.amount))

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return ElfArmy(self.amount - other.amount, self.damage, self.health, self.shield)
        else:
            return ElfArmy(0, self.damage, self.health, self.shield)

    def receive_damage(self, damage: int):
        died_elfs = ((self.amount * (self.health + self.shield)) / damage)
        if self.amount > died_elfs:
            self.amount = self.amount - died_elfs
            return (died_elfs)
        else:
            return (self.amount)

if __name__ == "__main__":
    first_army = ElfArmy(1000, 100, 100, 30)
    print(first_army.receive_damage(5000))



