from gameComponents import gameVars, color

computer = gameVars.choices

def weaponsame(status):
    if computer == gameVars.player:
        print(str(color.c3) + "tie! " + status + str(color.c5))
        # tie - nothing else to compare, so it"ll exit

def weaponrock(status):
    if gameVars.player == "rock":
        if computer == "paper":
            print(str(color.c7) + "you " + status + str(color.c5))
        else:
            print(str(color.c8) + "you " + status + str(color.c5))

def weaponpaper(status):
    if gameVars.player == "paper":
        if computer == "scissors":
            print(str(color.c7) + "you " + status + str(color.c5))
        else:
            print(str(color.c8) + "you " + status + str(color.c5))

def weaponscissors(status):
    if gameVars.player == "scissors":
        if computer == "rock":
            print(str(color.c7) + "you " + status + str(color.c5))
        else:
            print(str(color.c8) + "you " + status + str(color.c5))

    gameVars.player = False
