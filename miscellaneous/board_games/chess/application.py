import pygame
from constants import *
from player import Player
from game_board import GameBoard, PieceColor

#--------------------------------------------------------------------------------------------------------------
# Main Game Loop
#--------------------------------------------------------------------------------------------------------------
class Application:
    def __init__(self):
        self.player = Player(self)
        self.__CLI()

    def __CLI(self):
        while True:
            cmd = input("Input command: ")
            cmd_words = cmd.split()
            if cmd_words[0] == "help":
                print("\thelp : list all commands")
                print("\tlist : list all available players")
                print("\trequest [player] : request game with player")
                print("\texit : exit command-line interface")
            elif cmd_words[0] == "list":
                self.player.list_players()
            elif cmd_words[0] == "request":
                game_orientation = self.player.game_request(cmd_words[1])
                if game_orientation == None: continue
                game_orientation = PieceColor.WHITE if game_orientation == "white" else PieceColor.BLACK
                self.start_game(game_orientation)
            elif cmd == "exit":
                self.player.leave_player_directory()
                break
            else:
                print("Command not found. Type 'help' for list of commands.")
            # server interrupt sets player's game_trigger field to game_orientation, signalling main thread to initialise game
            game_orientation = self.player.get_game_trigger()
            if game_orientation:
                self.start_game(game_orientation)
                self.player.reset_game_trigger()

    def start_game(self, game_orientation):
        pygame.init()
        clock = pygame.time.Clock()
        board = GameBoard(game_orientation)
        turn = game_orientation
        screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess")
        board.draw(screen)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    move = board.process_click_event(screen, turn, pygame.mouse.get_pos())
                    if move:
                        self.player.make_move(move)
                        turn = PieceColor.BLACK if turn == PieceColor.WHITE else PieceColor.WHITE
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()

app = Application()

# TODO
#   when a move is received, visualise move, turnover
# run and debug player/server/opponent connections, expected behavior is as follows:
#   run server, P1 and P2 proccesses on separate terminals
#   enter P1 username, join server, enter P2 username, join server
#   list 
# work on move exchange (player makes move, notifies opponent, receives move, renders, and so on)
# run and debug move exchange and visualisation
# website project page + github project page (licensing, network diagrams, state machines, markdown with code segments, fix projects page)
# MORE FEATURES
#   check with red highlighting
#       if notified that king is in check, highlight red
#       if king in check and proposed move does not put king out of check, invalidate
#       if proposed move puts own king in check, invalidate
#       if proposed move is valid and puts own king out of check, unhighlight
#       if proposed move is valid and puts opponents king in check, notify opponent
#   initial pawn movement of 2 spaces can jump over pieces
#   pawn promotion, castling, en passant, 
#   audio, board style, resolution of 45x45px
#   what if player force quits
#   add custom packet structure (replace strings with bits)
#   add user accounts + authentication