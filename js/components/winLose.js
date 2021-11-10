function winorlose(status) {
    console.log("you " + status);

    let choice = prompt("do you want to play again? y/n: ");

    if (choice == "n") {
        console.log("========= see ya!🤩🤩 ==========");
        exit()
    } else if (choice == "y") {
        playerLives = 5;
        computerLives = 5;
        player = false;
    }
}

export { winorlose }