from gameComponents import gameVars, color


def winorlose(status):
    print("you " + status)

    choice = input(str(color.c4) + "do you want to play again?😍 y/n: ")

    if choice == "n":
        print(str(color.c6) + "=======see ya!🤩🤩========" + str(color.c5))
        exit()
    elif choice == "y":
        gameVars.playerLives = 3
        gameVars.computerLives = 3
        gameVars.player = False
