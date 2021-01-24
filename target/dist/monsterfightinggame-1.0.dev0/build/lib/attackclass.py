from random import randint


#This class is meant for creating monster attacks
class attack():
    A = 0
    N = ""
    def __init__(self):
        self.A = self.Attack()
        self.N = self.AttackName()


    # Function for attack three
    def Attack(self):
        a = randint(5, 30)
        return a
        pass

    # Function for finding the name of an attack
    def AttackName(self):
        Anames = [" Kick ", " Punch ", " Blast ", " Beam ", " Bite ", " Slash ", " Stab "]
        l = len(Anames)
        L = randint(0, l - 1)
        L1 = Anames[L]

        Dnames = ["Spinning", "Strong", "Powerful", "Furious", "Enraged", "Roaring", "Wicked",
                  "Scociopathic", "Uncle Charlie's", "Psychotic", "Wailing", "Roundhouse", "Dreaded", "Shocking",
                  "Annoying"]
        d = len(Dnames)
        D = randint(0, d - 1)
        D1 = Dnames[D]

        Fnames = ["of Power ", "of Strength", " of Innocence", "of Energy", "of Fire", "of Water", "of Earth", "of Air"]
        f = len(Fnames)
        F = randint(0, f - 1)
        F1 = Fnames[F]
        r = randint(0, 1)

        if r == 0:
            Thename = D1 + L1
        elif r == 1:
            Thename = D1 + L1 + F1

        return Thename

        pass

    pass

