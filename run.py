
class Board:
    """
    Creates the game board
    """
    def __init__(self):
        self.board = ['.'] * 16
    
    def to_string(self):
        return '{}|{}|{}|{}\n-------\n{}|{}|{}|{}\n-------\n{}|{}|{}|{}\n'.format(*self.board)
       

print(Board().to_string())


