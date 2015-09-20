__author__ = 'rohanmathure'


class InvalidInputException(Exception):
    def __init__(self, msg):
        self.msg = msg

class ChessTileOccupiedException(Exception):
    def __init__(self, msg):
        self.msg = msg