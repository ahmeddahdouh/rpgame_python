import random

from categories.stats import Stat


class Avatar:
    """general class"""

    id = 0

    def __init__(self, targs):
        self._nom = targs["name"]
        self._race = targs["race"]
        self._classe = targs["classe"]
        self._bag = targs["bag"]
        self._equipment = targs["equipment"]
        self._element = targs["element"]
        self._lvl = 1
        self._stat = Stat(
            {
                "strength": 1,
                "magic": 1,
                "agility": 1,
                "speed": 1,
                "charisma": 0,
                "chance": 0,
            }
        )
        Avatar.id += 1
        self.sumStat()
        self._life = self._stat.life_point

    def getBag(self):
        return self._bag._lItems

    def initiative(self):
        min = self._stat.speed
        max = self._stat.agility + self._stat.chance + self._stat.speed
        return random.randint(min, max)

    def damages(self):
        critique = random.randint(0, self._stat.chance)
        min = 0
        max = self._stat.attack
        if critique > self._stat.chance / 2:
            print("full damages")
            maxDam = random.randint(max, 2 * max)
        else:
            maxDam = random.randint(min, max)
        print(self._nom + " done " + str(maxDam))
        return maxDam

    def defense(self, v):
        min = self._stat.agility
        max = self._stat.agility + self._stat.chance + self._stat.speed
        duck = random.randint(min, max)
        damage = 0
        print(self._nom + " Duck " + str(duck))
        if duck == max:
            print("the shot is dodged")
        elif duck > max / 2:
            print("partial dodge")
            damage = v / 2
        else:
            damage = v
        damage -= self._stat.defense
        print(self._nom + " Puissance de défeence " + str(self._stat.defense))
        if damage < 0:
            damage = 0
        if damage > self._life:
            self._life = 0
            print("You are dead")
        else:
            self._life -= damage
        print("life point: ", self._life, " / ", self._stat.life_point)

    def __str__(self):
        show = str(self._nom)
        return show

    def sumStat(self):
        equiment = 0
        for i in self._stat.__dict__:
            for j in self._equipment:
                equiment += j._stat.__dict__[i]
            self._stat.__dict__[i] = (
                self._race._stat.__dict__[i] + self._classe._stat.__dict__[i] + equiment
            )
