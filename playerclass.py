from random import randint
from programclass import program
# This is the class for the player
class Player():

    name = ""
    health = 0
    action = 0

    # initializer
    def __init__(self):
        self.name = self.Name()
        self.health = self.Health()
        input("Press any key to continue:")

    # Gets the name of the player
    def Name(self):
        print("Hello young hero!")
        name = str(input("What is your name?"))
        print("Prepare to defeat monsters,", name, "!")
        return name

    # Gets the health of the player
    def Health(self):
        health = randint(50,100)
        print("Your health is:", health)
        return health

    # Gets the choice of the player
    def HitBlock(self):
        print("Would you like to hit or block?")
        choice = int(input("One for hit, 0 for block:"))
        return choice

    # Gets the attack damage of the player
    def Attack(self):
        a = randint(40,80)
        return a







