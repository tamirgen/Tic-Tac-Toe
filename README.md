# Tic-Tac-Toe Game
------------------

The Tic-Tac-Toe game is a Python game that runs on the mock terminal by Heroku.

It is a two players game and the target is to complete a line, column or a diagonal before the other player.
The game was design in order to develop the ability of a player to anticipate the other player moves and to 
prepare a strategy of winning using the minimum possible moves. 

[Here is a link to the live version of the game](https://tic-tac-toe-tamir.herokuapp.com/)

![Responsive Mockup](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/tic-tac-toe-AMIresponsive.jpg?raw=true)

<br>

## How to play
--------------

The game is based on the clasic Tick-Tac-Toe game. You can read more about the game on [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe).
In this version, the players are asked to enter their names, and the board is printed to the terminal numbered 0-8.
Each player is assigned a mark (x,o) and after each one places a mark on the board, using the keyboard, the turns are changing.
The board keeps the marks of each player and the player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. The game will declare a winner with the statement: "Congratulations {name}, you win".
If no one wins, a draw is announced and the game is over.

<br>

## Existing Features
--------------------

- This is a two players game.
- The players are being asked to enter their names.

<br>

![players names](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-ask-for-names.jpg?raw=true)

- The board is printed to the termianl numbered 0-8.
- An announcement is printed: "This is the current board,{name} please make a move 0-8\n')).

<br>

![board printed](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-show-board-and-inst.jpg?raw=true)

- Input validation:
  * Check if the number is between 0-8.
  * Check if the input is a number.
  * Check that the same number is entered twice.

 <br>

 ![validation check](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-illegal-moves.jpg?raw=true)

- If there is a winner, his name will be added to the winning sentence.
- If there is a draw, the termial will print: "No one wins! Better luck next time."

<br>

![winner announce](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

### Future Feature
------------------
- Add AI automation, so the player can play against the computer.

<br>

## Data Model
--------------

I have used three classes for this project:
- Board class is in charge of:
   * Creating the board.
   * Handling and checking the legal moves.
   * Checking turns between the players.

- Player class is in charge of:
   * Holding the players names and markers.
   * Getting information from a function in Board class and printing the illegal move statement.

- Game class is in charge of:
   * Swapping turns between players.
   * Holding the actual game.
   * Checking and announcing the winner or calling for a draw.

   <br>

## Testing
-----------

I have manualy tested my project by doing the following:
- Passed the code through PEP8 and made sure it is error free.
- Given invalid inputs: numbers that are not 0-8, letters instead of numbers and the same number twice.
- Tested in my local terminal and the Heroku terminal.
- Tested on an Android tablet and IOS smartphone.

<br>

## Bugs
--------

There were no bugs to fix.

<br>

## Deployment
--------------

The project was deployed using the Code Institute's mock terminal from Heroku.
Steps:
  * Create new app on Heroku.
  * Add a key: PORT and value: 8000 to the Config Vars.
  * Set the buildback to "Python" and "NodeJS" in that order.
  * Link the Heroku app to the project repository.
  * Click on <b>Deploy<b>

<br>

## Credit
----------
- Code Institue for the deployment terminal.
- Wikipedia for the details on Tic-Tac-Toe





