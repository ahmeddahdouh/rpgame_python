import random


class Stat:
    """stat of the player"""

    def __init__(self, dictArgs):
        self.strength = dictArgs["strength"]
        self.magic = dictArgs["magic"]
        self.agility = dictArgs["agility"]
        self.speed = dictArgs["speed"]
        self.charisma = dictArgs["charisma"]
        self.chance = dictArgs["chance"]
        self.endurance = random.randint(
            self.strength + self.agility, 2 * (self.strength + self.agility)
        )
        self.life_point = random.randint(self.endurance, 2 * self.endurance)
        self.attack = self.strength + self.magic + self.agility
        self.defense = self.agility + self.speed + self.endurance

    @property
    def strength(self):
        print("strength: ")
        return self._strength

    @strength.setter
    def strength(self, v):
        print("strength upgrade")
        self._strength = v

    def __str__(self):
        return str(self.__dict__)
