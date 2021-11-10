from random import randint
from gameComponents import winLose, gameVars, color


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    computer = gameVars.choices[randint(0, 2)]

    print(str(color.c1) + "player chose: " + gameVars.player)
    print(str(color.c2) + "computer chose: " + computer)

    if computer == gameVars.player:
        # tie - nothing else to compare, so it"ll exit
        print(str(color.c3) + "tie! try again😊" + str(color.c5))

    elif gameVars.player == "rock":
        if computer == "paper":
            print(str(color.c7) + "you lose!😭" + str(color.c5))
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(str(color.c8) + "you win!🥳" + str(color.c5))
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if computer == "scissors✂":
            print(str(color.c7) + "you lose!😭" + str(color.c5))
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(str(color.c8) + "you win!🥳" + str(color.c5))
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if computer == "rock":
            print(str(color.c7) + "you lose!😭" + str(color.c5))
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print(str(color.c8) + "you win!🥳" + str(color.c5))
            gameVars.computerLives = gameVars.computerLives - 1

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False
