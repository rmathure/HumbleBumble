__author__ = 'rohanmathure'


class InvalidInputException(Exception):
    def __init__(self, msg):
        self.msg = msg
        print msg

class ChessTileOccupiedException(Exception):
    def __init__(self, msg):
        self.msg = msg
        print msg

class PieceColorNotImplemented(Exception):
    def __init__(self, msg):
        self.msg = msg
        print msg