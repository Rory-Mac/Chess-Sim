from enum import Enum

PLAYER_DIRECTORY_ADDR = ('localhost', 18000)
PACKET_MAX_SIZE = 1024
TILE_WIDTH = 48

DARK_TILE = (69,77,95)
LIGHT_TILE = (230,234,215)
CHECKMATE_TILE = (153,28,54)
HIGHLIGHTED_DARK_TILE = (130,159,217)
HIGHLIGHTED_LIGHT_TILE = (190,212,232)

class PieceColor(Enum):
    LIGHT = 0
    DARK = 1

class PlayerStatus(Enum):
    ONLINE = 0
    INGAME = 1

class RequestType(Enum):
    SET_NAME = 0                    # payload :: username
    LIST_ALL = 1                    # payload :: None | player_list
    GAME_REQUEST = 2                # payload :: (user_from, user_to)
    ACCEPT_GAME = 3                 # payload :: user_from, listening_addr
    REJECT_GAME = 4                 # payload :: (user_from, user_to)
    INITIALISE_REQUESTING = 5       # payload :: (listening_addr, color)
    INITIALISE_REQUESTED = 6        # payload :: color
    MOVE = 6                        # payload :: ((x1,y1), (x2,y2))
    TERMINATE_GAME = 7              # payload :: None
    TERMINATE_GAME_ACK = 8          # payload :: None
    LEAVE_SERVER = 9                # payload :: None
    SUCCESS = 10                    # payload :: message
    FAILURE = 11                    # payload :: message