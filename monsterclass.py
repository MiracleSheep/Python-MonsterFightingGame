from random import randint
from attackclass import attack



# This is the class for the monster
class Monster():



# Initializer
    def __init__(self):
        self.h = self.Health()
        self.name = self.Name()
        self.A1 = attack()
        self.A2 = attack()
        self.A3 = attack()


        pass




# Function for Getting the health of the monster
    def Health(self):
        health = randint(1, 100)
        return health
    pass


# Function for getting the name of the monster
    def Name(self):
        Names = ["Ogre", "Serpent", "Troll", "Hydra", "Minotaur", "Zombie", "Skeleton" , "Creeper", "Dragon", "Vampire", "Witch" , "Wizard", "Sorcerer"]
        num = randint(0, len(Names))
        n = Names[num - 1]

        if self.h <= 70 and self.h >= 41:
            s = "Average"
        if self.h <= 40:
             s = "Weak"
        if self.h >= 71 and self.h <= 100:
            s = "Strong"

        Dnames = [" Vengeful ", " Enraged ", " Adorable ", " Annoying ", " Tired ", " Happy ", " Funny ", " Ridiculous ", " Depressed "]
        num2 = randint(0, len(Dnames))
        n2 = Dnames[num2 - 1]

        tname = s + n2 + n

        return tname




