from gameComponents import gameVars, color


def winorlose(status):
    print("you " + status)

    choice = input(str(color.c4) + "Do you want to play again?😍 y/n: ")

    if choice == "n":
        print(str(color.c6) + "=======see ya!🤩🤩========" + str(color.c5))
        exit()
    elif choice == "y":
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False
