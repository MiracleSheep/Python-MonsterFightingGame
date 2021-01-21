from gameclass import Game
from random import randint
# This is the class for the monster
class Monster(Game):

    def __init__(self):
        n = self.Name()
        c = self.Health()
        A1 = self.Attack1()
        A2 = self.Attack2()
        A3 = self.Attack3()

        pass

# function for Attack one
    def Attack1(self):
        a = randint(0, 5 - 30)
        return a
        pass

# Function for attack two
    def Attack2(self):
        a = randint(0, 5 - 30)
        return a
        pass

# Function for attack three
    def Attack3(self):
        a = randint(0, 5 - 30)
        return a
        pass

# Function for finding the name of an attack
    def AttackName(self):
        Anames = [" Kick "," Punch "," Blast ", " Beam ", " Bite ", " Slash ", " Stab "]
        l = len(Anames)
        L = randint(0,l)
        L1 = Anames[L]

        Dnames = ["Spinning", "Strong", "Powerful", "Furious", "Enraged" , "Roaring" , "Wicked",
                  "Scociopathic", "Uncle Charlie's", "Psychotic", "Wailing", "Roundhouse" , "Dreaded", "Shocking", "Annoying"]
        d = len(Dnames)
        D = randint(0,d)
        D1 = Dnames[D]

        Fnames = ["of Power ", "of Strength", " of Innocence", "of Energy", "of Fire", "of Water", "of Earth", "of Air"]
        f = len(Fnames)
        F = randint(0,f)
        F1 = Fnames[F]
        r = randint(0,1)


        if r == 0:
            Thename = L1+D1
        elif r == 1:
            Thename = L1+D1+F1

        return Thename





        pass



# Function for Getting the health of the monster
    def Health(self):
        health = randint(0, 100)
        return health
    pass


# Function for getting the name of the monster
    def Name(self):
        Names = [" Ogre ", " Serpent ", " Troll ", " Hydra ", " Minotaur ", " Zombie ", " Skeleton " , " Creeper ", " Dragon ", " Vampire ", " Witch " , " Wizard ", " Sorcerer "]
        num = randint(0, len(Names))
        n = Names[num]
        return n


