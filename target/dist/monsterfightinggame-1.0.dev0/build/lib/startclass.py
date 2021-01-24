from programclass import program


# This class contains functions for the start of the game
class start(program):

    def __init__(self):
        self.intro()
        self.tutorial()


    # This function calls the intro
    def intro(self):
        self.talk("Welcome!", 1)
        self.talk("In order to practice my skills of python, I have decided to create a monster fighting game.", 1)
        self.talk("In this game, you will have to defeat monsters!",1)


    # This function does the tutorial for the game
    def tutorial(self):
        self.talk("Would you like to take the tutorial?", 1)
        self.talk("Press 0 to decline and 1 to accept!", 1)
        self.talk("Enter your response below:", 1)


        cont = int(input())
        if cont == 1:
            self.talk("Tutorial it is!",1)
            self.talk("First, you get to choose your name, and the number of monsters you want to defeat", 3)
            self.talk("Your name is not important, but the number of monsters means how long the game will last.", 3)
            self.talk("Then you will be shown the name, attacks and health of the monster.", 3)
            self.talk("You will be given the choice to block, hit or feint.", 3)
            self.talk("This is very much like rock paper scissors.", 3)
            self.talk("In this game, blocking beats attack, attack beats feint, and feint beats blocking.",3)
            self.talk("The monster will also be able to block, attack and feint.", 3)
            self.talk("This continues until you have defeated all the monsters.", 3)
            input("Press enter to continue to the game.")

        elif cont == 0:
            self.talk("Alrighty then. Starting the game.",1)


        else:
            self.talk("That is not a valid response. Defaluting to no.",1)




