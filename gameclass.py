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
                num1 = randint(0, 2)

                if choice == 1:
                    self.talk("You decided to attack.",1)
                elif choice == 0:
                    self.talk("You decided to block.",1)
                elif choice == 2:
                    self.talk("You decided to feint.",1)

                self.talk("It is now the monster's turn.",1)

                if num1 == 1:
                    self.talk("the monster chooses to block",1)

                elif num1 == 0:
                    self.talk("The monster chooses to attack!",1)

                elif num1== 2:
                    self.talk("The monster chooses to feint!",1)


                num = randint(0, 2)
                if num == 1:
                  Attack = m.A1
                elif num == 0:
                    Attack = m.A2
                elif num == 2:
                    Attack = m.A3



                if (choice == 1 and num1 == 1):
                    a = p.Attack()
                    self.talk("You attack first!",1)
                    print("You deal",a,"Damage!")
                    self.talk("The monster braces themselves so they take none of your damage.",1)
                    self.talk("You are stunned and take damage!",1)
                    p.health = p.health = Attack.A
                elif(choice == 1 and num1 == 0):
                    a = p.Attack()
                    self.talk("Both of you decided to attack!",1)
                    print("Your attack and the monster's", Attack.N,"parry eachother.")
                    if m.h <= 0:
                        print("The ", m.name, " has been defeated!")
                        MDefeated = True
                        defeated += 1

                    if p.health <= 0:
                        print("You have been defeated by the ", m.name, ".")
                        self.talk("Better luck next time!", 1)
                        PDefeated = True
                        return
                elif (choice == 1 and num1 == 2):
                    print("The monster feints, using", Attack.N, "but you attack more directly, landing a direct hit!")

                    m.h = m.h - p.Attack()
                    if m.h <= 0:
                        print("The ", m.name, " has been defeated!")
                        MDefeated = True
                        defeated += 1

                    if p.health <= 0:
                        print("You have been defeated by the ", m.name, ".")
                        self.talk("Better luck next time!", 1)
                        PDefeated = True
                        return


                elif(choice == 0 and num1 == 0):
                    self.talk("You brace yourself.",1)
                    print("The",m.name,"uses the attack ", Attack.N)
                    self.talk("The monster is stunned by your rebuttal and takes damage!",1)
                    m.h = m.h - p.Attack()
                elif(choice == 0 and num1 == 1):
                    self.talk("Both of you block!",1)
                    self.talk("Now you look kind of stupid...",1)
                elif (choice == 0 and num1 == 2):
                    print("The monster feints using the attack",Attack.N,"and you block instictively, allowing the monster to strike you elsewhere")
                    p.health = p.health - Attack.A
                    if m.h <= 0:
                        print("The ", m.name, " has been defeated!")
                        MDefeated = True
                        defeated += 1

                    if p.health <= 0:
                        print("You have been defeated by the ", m.name, ".")
                        self.talk("Better luck next time!", 1)
                        PDefeated = True
                        return
                elif (choice == 2 and num1 == 0):
                    print("As you feint the", m.name,"attacks directly using",Attack.N ,", dealing a direct hit!")
                    p.health = p.health - Attack.A
                    if m.h <= 0:
                        print("The ", m.name, " has been defeated!")
                        MDefeated = True
                        defeated += 1

                    if p.health <= 0:
                        print("You have been defeated by the ", m.name, ".")
                        self.talk("Better luck next time!", 1)
                        PDefeated = True
                        return
                elif (choice == 2 and num1 == 1):
                    self.talk("You feint an attack and the monster blocks instictively, allowing you to attack elsewhere!",1)
                    m.h = m.h - p.Attack()
                    if m.h <= 0:
                        print("The ", m.name, " has been defeated!")
                        MDefeated = True
                        defeated += 1

                    if p.health <= 0:
                        print("You have been defeated by the ", m.name, ".")
                        self.talk("Better luck next time!", 1)
                        PDefeated = True
                        return
                elif (choice == 2 and num1 == 2):
                    self.talk("Both of you feint, and your attacks parry eachother!",1)

                if p.health <= 0:
                    print("You have been defeated by the ", m.name , ".")
                    self.talk("Better luck next time!",1)
                    PDefeated = True
                    return


            if PDefeated == True:
                return




            if defeated >= length:
                print("Congradulations,", p.name, "!")
                self.talk("All the monsters have been defeated!",1)
                self.talk("You will be worshipped as a hero for years to come!",1)
                Gameon = False






# function that gets the length of the gamne from the player

    def Gamelength(self):
        while True:
            num = 1
            try:
                self.talk("How many monsters do you want in this game?", 1)
                num = int(input("Enter the amount here:"))
            except:
                num = 1

            if (num <= 0):
                self.talk("That is not an appropriate response!")
            else:
                return num


            return num

        pass

