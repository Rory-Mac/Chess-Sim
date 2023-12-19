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
    JOIN_SERVER = 0                 # not used (marker for server logs)
    SET_NAME = 1                    # payload :: username
    LIST_ALL = 2                    # payload :: None | player_list
    GAME_REQUEST = 3                # payload :: (user_from, user_to)
    ACCEPT_GAME = 4                 # payload :: user_from, listening_addr
    REJECT_GAME = 5                 # payload :: (user_from, user_to)
    INITIALISE_REQUESTING = 6       # payload :: (listening_addr, color)
    INITIALISE_REQUESTED = 7        # payload :: color
    MOVE = 8                        # payload :: ((x1,y1), (x2,y2))
    TERMINATE_GAME = 9              # payload :: None
    TERMINATE_GAME_ACK = 10         # payload :: None
    LEAVE_SERVER = 11               # payload :: None
    SUCCESS = 12                    # payload :: message
    FAILURE = 13                    # payload :: message