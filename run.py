
class Game:
    """
    Run the game and swapping turns between 2 palyers
    """
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.turn = False

    def play(self):
        while True:
            current_player = self.players[int(self.turn)]
 
            print(self.board.to_string())
            move = int(input(f'this is the current board, {current_player.name}make a move 0-8.\n'))
            while True:
                try:
                    is_winner = self.board.make_move(current_player, move)
                    break
                except (ValueError, IndexError):
                    move = int(input('Illegal move, please try again.\n'))
            if is_winner or self.board.is_draw():
                break
 
            self.turn = not self.turn
        print(self.board.to_string())
        if is_winner:
            print(f'Congratulations {current_player.name}, you win!')
        else:
            print('It\'s a draw!')

class Board:
    """
    Creates the game board.
    """
    def __init__(self):
        self.board = [' '] * 9
   
    def to_string(self):
        return '{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(*self.board)

    def make_move(self, player, place):
        """
        Choose a palce and make sure that there are no mistakes
        """
        if self.board[place] != ' ':
            raise ValueError(f'The place{place} is taken.')
        self.board[place] = player.marker
        return self.is_winner(player.marker)

    def is_winner(self, marker):
        """
        Check winning combinations
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

        return any([all([self.board[x] == marker for x in pos]) for pos in winning_positions])

    def is_draw(self):
        """
        Check if the board is full and call for a draw.
        """
        return ' ' not in self.board    

       
class Player:
    """
    Creates a player and his marker.
    """
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

            
name1 = input('Enter the first player name:\n')
name2 = input('Enter the second player name:\n')
            
Game(Player(name1, 'x'), Player(name2, 'o')).play()




