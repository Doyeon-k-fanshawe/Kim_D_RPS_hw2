import { winorlose } from "./components/winLose.js";

(() => {
	// IIFE (immediately invoked fuction expression)
	const choices = ["rock", "paper", "scissors"]

	// player will be the weapon the player chooses via input

	let player = false,
		playerLives = 2,
		computerLives = 2,
		button = document.querySelector("button");

	function gameLoop() {
		player = prompt("Choose your weapon: rock, paper or scissors: ");

    	computer = choices[Math.floor(Math.random() * 3)];

    	console.log("player chose: " + player);
    	console.log("computer chose: " + computer);

    	if (computer == player) {
        	// tie - nothing else to compare, so it'll exit
        	console.log("tie! try again😊");
        	return;
        }

        if (player == "rock") {
        	if (computer == "paper") {
            	console.log("you lose!😭");
            	playerLives --; 
            	//decrement operator -> subtract 1 from the current value
        	} else {
            	console.log("you win!🥳");
            	computerLives --;
            }
		}

		if (player == "paper") {
			if (computer == "scissors") {
				console.log("you lose!😭");
            	playerLives --;
			} else {
				console.log("you win!🥳");
            	computerLives --;
			}
		}
        
        if (player == "scissors") {
			if (computer == "rock") {
				console.log("you lose!😭");
            	playerLives --;
			} else {
				console.log("you win!🥳");
            	computerLives --;
			}
		}

		console.log("player life count:", playerLives);
    	console.log("computer life count:", computerLives);
	
		if (playerLives == 0) {
	        winorlose("lost");
		} else if (computerLives == 0) {
	        winorlose("won");
		}
	}

	button.addEventListener("click", gameLoop);
}) ();