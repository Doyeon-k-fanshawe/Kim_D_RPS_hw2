from random import randint
from gameComponents import winLose, gameVars


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:

    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    computer = gameVars.choices[randint(0, 2)]

    print("\033[92m" + "player chose: " + gameVars.player)
    print("\033[96m" + "computer chose: " + computer)

    if computer == gameVars.player:
        # tie - nothing else to compare, so it'll exit
        print('\033[95m' + 'tie! ' + '\033[96m' + 'try again😊' + '\033[0m\n')

    elif gameVars.player == "rock":
        if computer == "paper":
            print('\033[90m' + 'you ' + '\033[91m' + 'lose!😭' + '\033[0m\n')
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print('\033[90m' + 'you ' + '\033[94m' + 'win!🥳' + '\033[0m\n')
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if computer == "scissors✂":
            print('\033[90m' + 'you ' + '\033[91m' + 'lose!😭' + '\033[0m')
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print('\033[90m' + 'you ' + '\033[94m' + 'win!🥳' + '\033[0m\n')
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if computer == "rock":
            print('\033[90m' + 'you ' + '\033[91m' + 'lose!😭' + '\033[0m\n')
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print('\033[90m' + 'you ' + '\033[94m' + 'win!🥳' + '\033[0m\n')
            gameVars.computerLives = gameVars.computerLives - 1

    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
        winLose.winorlose("won")

    gameVars.player = False
