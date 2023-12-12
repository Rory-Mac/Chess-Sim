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

class PlayerStatus(Enum):
    ONLINE = 0
    INGAME = 1

class RequestType(Enum):
    SET_NAME = 0            # payload :: username
    LIST_ALL = 1            # payload :: None
    GAME_REQUEST = 2        # payload :: (user_from, user_to)
    ACCEPT_GAME = 3         # payload :: listening_addr
    REJECT_GAME = 4         # payload :: None
    INITIALISE_GAME = 5     # payload :: (listening_addr, color)
    MOVE = 6                # payload :: (x1,y1), (x2,y2)
    LEAVE_SERVER = 7        # payload :: None
    SUCCESS = 8             # payload :: message
    FAILURE = 9             # payload :: message