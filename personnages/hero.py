import math
from datetime import date

from personnages.avatar import Avatar


class Hero(Avatar):
    def __init__(self, targs):
        Avatar.__init__(self, targs)
        self._xp = 1
        self._profession = targs["profession"]
        self._lvl = self.lvl()

    def lvl(self):
        lvl = math.floor(self._xp / 100)
        if lvl < 1:
            lvl = 1
        if lvl > self._lvl:
            print("### new level ###")
            self.newLvl()
        return lvl

    def newLvl(self):
        for i in self._stat.__dict__:
            self._stat.__dict__[i] += 5
        self._life = self._stat.life_point
        print("### stats upgrade ###")

    def setXP(self, xp):
        self._xp += xp
        self._lvl = self.lvl()

    def __str__(self):
        output = (
            "joueur "
            + self._nom
            + " de niveau "
            + str(self._lvl)
            + " classe "
            + str(self._classe)
            + " race "
            + str(self._race)
        )
        return output

    def save(self):
        fileName = (
            str(date.today()) + "_" + str(Hero.id) + "_" + str(self._nom) + ".txt"
        )
        f = open(fileName, "w+")
        f.write(self._nom + "\n")
        f.write(self._race._name + "\n")
        f.write(self._classe._name + "\n")
        f.write("lvl: " + str(self._lvl) + "\n")
        f.write("xp: " + str(self._xp) + "\n")
        for i in self._stat.__dict__:
            output = str(i) + " " + str(self._stat.__dict__[i])
            f.write(output + "\n")
        for i in self._equipment:
            f.write(str(i) + "\n")
        for i in self.getBag():
            f.write(str(i) + "\n")
        f.close()

    def saveXML(self):
        fileName = (
            str(date.today()) + "_" + str(Hero.id) + "_" + str(self._nom) + ".xml"
        )
        f = open(fileName, "w+")
        xml = "<?xml version='1.0' encoding='UTF-8'?>"
        xml += "<avatar id='" + str(Hero.id) + "'>"
        xml += "<name>" + self._nom + "</name>"
        xml += "<race>" + self._race._name + "</race>"
        xml += "<level>" + self._classe._name + "</level>"
        xml += "<xp>" + str(self._lvl) + "</xp>"
        xml += "<name>" + str(self._xp) + "</name>"
        xml += "<stats>"
        for i in self._stat.__dict__:
            xml += (
                "<" + str(i) + ">" + str(self._stat.__dict__[i]) + "</" + str(i) + ">"
            )
        xml += "</stats>"
        xml += "<equipments>"
        it = 1
        for i in self._equipment:
            xml += "<item_" + str(it) + ">" + i._name + "</item_" + str(it) + ">"
            it += 1
        xml += "</equipments>"
        xml += "<bag>"
        it = 1
        for i in self.getBag():
            xml += "<item_" + str(it) + ">" + i._name + "</item_" + str(it) + ">"
            it += 1
        xml += "</bag>"
        xml += "</avatar>"
        f.write(xml)
        f.close()

    @staticmethod
    def load():
        pass
