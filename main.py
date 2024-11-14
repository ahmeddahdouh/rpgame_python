from itertools import combinations

from equipments.bag import Bag
from equipments.equipment import Equipment
from jeu.quest import Quest
from joueurs.joueur import joueur
from jeu.plateau import Plateau
from personnages.hero import Hero
from equipments.item import Item
from personnages.mobs import Mobs
from categories.race import Race
from categories.stats import Stat


def main():

    ### RACE
    statElfe = Stat(
        {
            "strength": 5,
            "magic": 10,
            "agility": 10,
            "speed": 5,
            "charisma": 5,
            "chance": 5,
        }
    )
    elfe = Race("Elfe", statElfe)
    statHuman = Stat(
        {
            "strength": 10,
            "magic": 10,
            "agility": 5,
            "speed": 5,
            "charisma": 5,
            "chance": 5,
        }
    )
    human = Race("Human", statHuman)
    statDwarf = Stat(
        {
            "strength": 10,
            "magic": 0,
            "agility": 10,
            "speed": 5,
            "charisma": 5,
            "chance": 10,
        }
    )
    dwarf = Race("Dwarf", statDwarf)
    statOrc = Stat(
        {
            "strength": 15,
            "magic": 0,
            "agility": 5,
            "speed": 10,
            "charisma": 5,
            "chance": 5,
        }
    )
    orc = Race("Orc", statOrc)
    ### CLASS
    statWizard = Stat(
        {
            "strength": 0,
            "magic": 10,
            "agility": 0,
            "speed": 0,
            "charisma": 10,
            "chance": 10,
        }
    )
    wizard = Race("Wizard", statWizard)
    statWarrior = Stat(
        {
            "strength": 10,
            "magic": 0,
            "agility": 5,
            "speed": 5,
            "charisma": 5,
            "chance": 5,
        }
    )
    warrior = Race("Warrior", statWarrior)
    ### ITEMS
    statSword = Stat(
        {
            "strength": 5,
            "magic": 0,
            "agility": 5,
            "speed": 5,
            "charisma": 0,
            "chance": 5,
        }
    )
    sword = Equipment(
        {
            "classList": "warrior",
            "place": "hand",
            "name": "dragon sword",
            "type": "sword",
            "space": 2,
        },
        statSword,
    )
    statBaton = Stat(
        {
            "strength": 0,
            "magic": 10,
            "agility": 0,
            "speed": 5,
            "charisma": 0,
            "chance": 5,
        }
    )
    baton = Equipment(
        {
            "classList": "wizard",
            "place": "hand",
            "name": "wizard baton",
            "type": "baton",
            "space": 2,
        },
        statBaton,
    )
    statPotion = Stat(
        {
            "strength": 0,
            "magic": 0,
            "agility": 0,
            "speed": 0,
            "charisma": 0,
            "chance": 0,
        }
    )
    Potion = Item(
        {
            "name": "life potion",
            "type": "potion",
            "space": 2,
        },
        statPotion,
    )
    ### BAG
    myBag = Bag({"sizeMax": 20, "items": [Potion, Potion]})
    ### MOBS
    mechant1 = Mobs(
        {
            "name": "orc 1",
            "race": orc,
            "classe": warrior,
            "bag": myBag,
            "equipment": [sword],
            "element": "Fire",
            "type": "soldier",
        }
    )
    mechant2 = Mobs(
        {
            "name": "orc 2",
            "race": orc,
            "classe": warrior,
            "bag": myBag,
            "equipment": [sword],
            "element": "Fire",
            "type": "soldier",
        }
    )
    hero1 = Hero(
        {
            "name": "Jean",
            "race": elfe,
            "classe": wizard,
            "bag": myBag,
            "equipment": [baton],
            "element": "Fire",
            "profession": "chomeur",
        }
    )
    hero2 = Hero(
        {
            "name": "Pierre",
            "race": human,
            "classe": warrior,
            "bag": myBag,
            "equipment": [sword],
            "element": "Fire",
            "profession": "chomeur",
        }
    )

    # ---PLATEAU---#

    plateau = Plateau("Partie 1", 12, 3)
    while True:
        try:
            nbr_joueurs = int(
                input(f"Entrez un nombre entier entre 1 et {plateau.NB_JOUEUR_MAX}: ")
            )
            if 1 <= nbr_joueurs <= plateau.NB_JOUEUR_MAX:
                break
            else:
                print(f"Le nombre doit être entre 1 et {plateau.NB_JOUEUR_MAX}.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

    # ---JOUEURS---#
    joueurs = []
    personnages = [mechant1, mechant2, hero1, hero2]
    combinaisons = [list(combinaison) for combinaison in combinations(personnages, 2)][
        :nbr_joueurs
    ]

    for i in range(nbr_joueurs):
        nom_joueur = input(f"Entrez le nom du joueur {i + 1} : ")
        joueur_obj = joueur(nom=nom_joueur, listperso=combinaisons[i])
        plateau.ajouter_joueur(joueur_obj)
        joueurs.append(joueur_obj)

    # Affichage des joueurs créés pour vérification
    for i, joueur_obj in enumerate(joueurs, start=1):
        print(f"Joueur {i}: {str(joueur_obj)}")

    plateau.initialiser_cases()
    plateau.lancer_jeu()

    plateau.afficher_plateau()

    # hero1.save()
    # hero1.saveXML()
    # ### QUEST
    # firstQuest = Quest({'lAvatar': [mechant1, mechant2], 'lvl': 2, 'gift': sword})
    # # firstQuest = Quest({'lAvatar':[hero2],'lvl':2,'gift':sword})
    # firstQuest.run(hero1)


if __name__ == "__main__":
    # execute only if run as a script
    main()
