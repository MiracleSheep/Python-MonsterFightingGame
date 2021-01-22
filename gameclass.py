from programclass import program
from monsterclass import Monster
from playerclass import Player
from random import randint


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
            i = input("Press enter to continue")

            MDefeated = False
            PDefeated = False
            while MDefeated == False and PDefeated == False:

                print("Your health is:", p.health)
                print("The ", m.name, "'s health is:", m.h)
                choice = p.HitBlock()
                num1 = randint(0, 1)

                if choice == 1:
                    print("You decided to attack.")
                else:
                    print("You decided to block.")
                    pass

                self.talk("It is now the monster's turn.",1)

                if (num1 == 1):
                    print("the monster chooses to block")

                else:
                    print("The monster chooses to attack!")


                num = randint(0, 2)
                if num == 1:
                  Attack = m.A1
                elif num == 0:
                    Attack = m.A2
                elif num == 2:
                    Attack = m.A3



                if (choice == 1 and num1 == 1):
                    a = p.Attack()
                    print("You attack first!")
                    print("You deal",a,"Damage!")
                    print("The monster braces themselves so they take none of your damage.")
                elif(choice == 1 and num1 == 0):
                    a = p.Attack()
                    print("You attack first!")
                    print("You deal",a,"Damage!")
                    m.h = m.h - p.Attack()
                    if m.h <= 0:
                        print("The ", m.name, " has been defeated!")
                        MDefeated = True
                        defeated += 1
                    else:
                        print("The", m.name, "retaliates!")
                        print("The", m.name, "uses the attack ", Attack.N)
                        print("You take ", Attack.A, " points of damage.")

                    p.health = p.health - Attack.A
                    if p.health <= 0:
                        print("You have been defeated by the ", m.name, ".")
                        self.talk("Better luck next time!", 1)
                        PDefeated = True
                        return
                elif(choice == 0 and num1 == 0):
                    print("You brace yourself.")
                    print("The",m.name,"uses the attack ", Attack.N)
                    print("You take 0 points of damage.")
                elif(choice == 0 and num1 == 1):
                    print("Both of you block!")
                    print("Now you look kind of stupid...")


                if p.health <= 0:
                    print("You have been defeated by the ", m.name , ".")
                    self.talk("Better luck next time!",1)
                    PDefeated = True
                    return


            if PDefeated == True:
                return




            if defeated >= length:
                Gameon = False






# function that gets the length of the gamne from the player

    def Gamelength(self):
        self.talk("How many monsters do you want in this game?",1)
        num = int(input("Enter the amount here:"))
        return num
        pass


    def IsGameWon(self):
        pass
