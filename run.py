

class Board:
    """
    Creates the game board.
    """
    def __init__(self, from_board=None):
        """
        Define the amount of cells in the board.
        """
        self.board = (from_board or list('012345678')).copy()

    def to_string(self):
        """
        Create the actual board as it appears on the terminal.
        """
        return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(
            *self.board)

    def place_mark(self, marker, place):
        """
        This function is checking if the value is between 0-8.
        """
        self.board[place] = marker
        return self.is_winner(marker)

    def legal_move(self, i):
        """
        This function is checking if the move is legal or the spot is already
        taken.
        """
        is_legal = True
        try:
            val = int(i)
            if val < 0 or val > 8:
                is_legal = False
            elif self.board[val] not in '012345678':
                is_legal = False
        except ValueError:
            is_legal = False
        finally:
            return is_legal

    def is_winner(self, marker):
        """
        Check all possible winning combinations.
        This fuction is checikg if the full list = True 
        and decides if there is a winner.
        """
        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
            ]

        return any([sum([self.board[i] == marker for i in pos]) == 3 
        for pos in winning_positions])

    def is_draw(self):
        """
        Check if the board is full and call for a draw.
        The function checks if all [i] in this range are full.
        """
        return all(str(i) not in self.board for i in range(8)) 

class Player:
    """
    Creates a player and his marker.
    """
    def __init__(self, name, marker):
        """
        The function that holds the palyer name and his marker(x,o)
        """
        self.name = name
        self.marker = marker
    
    def make_move(self, board):
        """
        This fuction is checking if the moves legal.
        Using a while loop, the player will be asked to try again
        until he puts a correct move 0-8.
        """
        move = input(
            f'This is the current board,{self.name} please make a move 0-8\n')

        while True:
            if board.legal_move(move):
                return int(move)
            else:
                move = input('Illegal move, please try again.\n')
           
        
class Game:
    """
    Run the game and swapping turns between 2 palyers
    """
    def __init__(self, player1, player2):
        """
        This function will create a new board for a new game.
        It will set a game for 2 players.
        It will decide who's turn is it.
        """
        self.board = Board()
        self.players = [player1, player2]
        self.turn = False

        self.play()    

    def play(self):
        """
        This function is the actual game.
        The while loop will print the board. 
        It states the name of the current player and which move he can make.
        The loop checks for winner or draw and break if find one.
        Outside the loof an if\esle can print the right outcome.
        """ 
        while True:
            current_player = self.players[int(self.turn)]
 
            print(self.board.to_string())
            move = current_player.make_move(self.board)
            is_winning = self.board.place_mark(current_player.marker, move)
            if is_winning or self.board.is_draw():
                break
            self.turn = not self.turn

        if self.board.is_draw():
            print('No one wins! Better luck next time.')
        else:
            print(f'Congratulations {current_player.name}, you win')
        print(self.board.to_string())    

name1 = input('Enter the first player name:\n')
name2 = input('Enter the second player name:\n')
            
Game(Player(name1, 'x'), Player(name2, 'o')).play()




