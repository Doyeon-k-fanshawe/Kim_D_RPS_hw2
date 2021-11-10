![rps game](rps.jpg "RPS Game")

# Rock Paper Scissors Game with Python!

TODO: Creating Rock Paper Scissors game with python.

Rock Paper Scissors in Python

==============================

A choosing game with three options. The player will choose one of 3 options; the computer / AI will choose one of the same 3 at random and then compare those 2 choices. 

The loser loses a life; the game will play on a loop until one player loses all lives.

Approach: 
Hold the options in an array: [“rock”, “paper”, “scissors”]
The Player’s choice has to be stored in a variable as well -> “rock”, “paper”, “scissors”
provide the user input via a text prompt => Done!
Let the computer choose at random
Figure out the path to win and lose

When comparing, some rules to follow: 

Rock beats scissors
Rock loses to paper

If (player == “rock”)
    What did the computer pick?
    If it’s paper, we lose
    If it’s scissors, we win
    If it’s a tie, play again

Scissors beats paper
Scissors loses to rock

Paper beats rock
Paper loses to scissors

If the player loses a round
    Lose a life
Else we win!
    AI loses a life



Things to consider:
What happens if a user misspells a choice?
What happens if it’s a tie?
What if a user doesn’t want to finish the game?
What if they don’t type the whole word?

How do you win? => figure out how to create  What happens when you run out of lives?


## Installation

TODO: Describe the installation process

## Usage

TODO: Write usage instructions

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D


## Credits

TODO: Write credits
// give accreditation to any resources / authors whose work you're using

## License

MIT