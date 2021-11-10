from gameComponents import gameVars


def winorlose(status):
    print("you " + status)

    choice = input('\033[36m' + 'do you want to play again?😍 y/n: ')

    if choice == "n":
        print('\033[92m' + '========= see ya!🤩🤩  ==========' + '\033[0m\n')
        exit()
    elif choice == "y":
        gameVars.playerLives = 3
        gameVars.computerLives = 3
        gameVars.player = False