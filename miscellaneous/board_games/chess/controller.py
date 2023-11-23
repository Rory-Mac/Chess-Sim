class GameController:
    def __init__(self):
        self.board = GameBoard()
        self.game = GameScreen()

    def makeMove(self):
        # move str of the form [file-rank file-rank] e.g. "a4 b3" meaning move piece positioned at a4 to b3, if valid
        position_from, position_to = input("Input next move: ").split()
        x_from, y_from = rank_to_x(position_from[1]), file_to_y(position_from[0])
        x_to, y_to = rank_to_x(position_to[1]), file_to_y(position_to[0])
        if not self.board.makeMove((x_from, y_from),(x_to, y_to)):
            print("Invalid Move.")


# TODO
# pygame visualiser
# mate and checkmate
# en passant
# separate machines on separate networks
# verse AI player