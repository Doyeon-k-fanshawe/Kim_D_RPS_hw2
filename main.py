from random import randint
from gameComponents import winLose, gameVars, color, comparePlayers


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    computer = gameVars.choices[randint(0, 2)]

    print(str(color.c1) + "player chose: " + gameVars.player)
    print(str(color.c2) + "computer chose: " + computer)

    if computer == gameVars.player:
        comparePlayers.weaponsame("try again😊")

    if gameVars.player == "rock":
        if computer == "paper":
            comparePlayers.weaponrock("lose!😭")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            comparePlayers.weaponrock("win!🥳")
            gameVars.computerLives = gameVars.computerLives - 1

    if gameVars.player == "paper":
        if computer == "scissors":
            comparePlayers.weaponpaper("lose!😭")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            comparePlayers.weaponpaper("win!🥳")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if computer == "rock":
            comparePlayers.weaponscissors("lose!😭")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            comparePlayers.weaponscissors("win!🥳")
            gameVars.computerLives = gameVars.computerLives - 1

    # invoke the function here (and maybe pass an argument to it.)

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost😭")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won🥳")

    gameVars.player = False
