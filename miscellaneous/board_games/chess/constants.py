from enum import Enum

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PLAYER_DIRECTORY_ADDR = ('localhost', 18000)
PACKET_MAX_SIZE = 1024

class PieceColor(Enum):
    WHITE = 0
    BLACK = 1
