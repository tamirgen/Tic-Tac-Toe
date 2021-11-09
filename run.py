
class Board:
    """
    Creates the game board
    """
    def __init__(self):
        self.board = ['.'] * 16
    
    def to_string(self):
        return '{}|{}|{}|{}\n-------\n{}|{}|{}|{}\n-------\n{}|{}|{}|{}\n'.format(*self.board)

    def make_move(self, player, place):
        """
        Choose a palce and make sure that there are no mistakes
        """
        if self.board[place] != '.':
            raise ValueError(f'The place{place} is taken.')
        self.board[place] = player.marker
        return self.is_winner(player.marker)

    def is_winner(self, marker):
        """
        Check winning combinations
        """
        winning_positions = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16],
            [1,5,9,13],
            [2,6,10,14],
            [3,7,11,15],
            [4,8,12,16],
            [1,6,11,16],
            [4,7,10,13],
           
            ]
        return any([all([self.board[x] == marker for x in pos]) for pos in winning_positions])

       
class Player:
    """
    Creates a player
    """
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
       
class Game:
    """
    Run the game and swapping turns between 2 palyers
    """
    def __init__(self, player1, player2):
        self.board = Board()
        self.player = [player1, player2]
        self.turn = False

    def play(self):
        while True:
            current_player = self.player[int(self.turn)]

            print(self.board.to_string())
            move = int(input(f'this is the current board, {current_player.name} make a move 0-15.\n'))
            while True:
                """
                This Loop is checking if there is a winner and if the palyers made a legal move
                """
                try:
                    is_winner = self.make_move(current_player, move)
                    break
                except ValueError:
                    move = int(input('Ilegal move, pleae try again.'))
                if is_winner:
                    break    


            self.turn = not self.turn


Game(Player('Tom', 'x'), Player('Regina', '0')).play()



