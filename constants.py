from enum import Enum

DARK_TILE = (119,153,84)
LIGHT_TILE = (233,237,204)
HIGHLIGHTED_DARK_TILE = (187,204,68)
HIGHLIGHTED_LIGHT_TILE = (244,246,128)
#DARK_TILE = (13,31,67)
#LIGHT_TILE = (0,71,135)
#HIGHLIGHTED_DARK_TILE = (130,159,217)
#HIGHLIGHTED_LIGHT_TILE = (190,212,232)

PLAYER_DIRECTORY_ADDR = ('localhost', 18000)
PACKET_MAX_SIZE = 1024

class PieceColor(Enum):
    WHITE = 0
    BLACK = 1

class PlayerStatus(Enum):
    ONLINE = 0
    INGAME = 1

class RequestType(Enum):
    SET_NAME = 0                    # payload :: username
    LIST_ALL = 1                    # payload :: none | player_list
    GAME_REQUEST = 2                # payload :: (user_from, user_to)
    ACCEPT_GAME = 3                 # payload :: user_from, listening_addr
    REJECT_GAME = 4                 # payload :: (user_from, user_to)
    INITIALISE_REQUESTING = 5       # payload :: (listening_addr, color)
    INITIALISE_REQUESTED = 6        # payload :: color
    MOVE = 6                        # payload :: (x1,y1), (x2,y2)
    LEAVE_SERVER = 7                # payload :: None
    SUCCESS = 8                     # payload :: message
    FAILURE = 9                     # payload :: message