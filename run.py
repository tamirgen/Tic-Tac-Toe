
class Board:
    """
    Creates the game board
    """
    def __init__(self):
        self.board = ['.'] * 16
    
    def to_string(self):
        return '{}|{}|{}|{}\n-------\n{}|{}|{}|{}\n-------\n{}|{}|{}|{}\n'.format(*self.board)
       
class Player:
    """
    Creates a player
    """
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker
       


print(Board().to_string())


