from programclass import program
from monsterclass import Monster
from playerclass import Player


# This is the class for the game
class Game(program):


    def __init__(self):

        Gameon = True

        length = self.Gamelength()
        defeated = 0
        p = Player()


        while Gameon == True:



            m = Monster()
            self.talk("A monster has approached you!",1)
            self.talk("Stats:",1)
            print("   Name:", m.name)
            print("   Health:", m.h)
            print("   Attacks:" )
            print("      Attack one:", m.A1.N)
            print("      Attack two:", m.A2.N)
            print("      Attack three:", m.A3.N)
            i = input("Press any key to continue")

            MDefeated = False
            PDefeated = False
            while MDefeated == False and PDefeated == False:

                print("Your health is:", p.health)
                choice = p.HitBlock()

                if choice == 1:
                    m.h = m.h - p.Attack()
                    print("You decided to attack. The ", m.name,"'s health is now ", m.h)
                else:
                    pass

                if m.h <= 0:
                    print("The ", m.name, " has been defeated!")
                    MDefeated = True
                    defeated += 1
                    return

                self.talk("It is now the monster's turn.",1)
                Attack = m.Attack()
                print("The monster uses the attack ", Attack.AttackName())
                print("You take " , Attack.Attack(), " points of damage.")
                p.health = p.health - Attack.Attack()

                if p.health <= 0:
                    print("You have been defeated by the ", m.name , ".")
                    self.talk("Better luck next time!",1)
                    PDefeated = True
                    return

            if PDefeated == True:
                Gameon = False
                return




            if defeated >= length:
                Gameon = False


            pass

        pass

# function that gets the length of the gamne from the player

    def Gamelength(self):
        self.talk("How many monsters do you want in this game?",1)
        num = int(input("Enter the amount here:"))
        return num
        pass


    def IsGameWon(self):
        pass
