import re
import time
import pygame
from constants import *
from player import Player
from game_board import GameBoard

#--------------------------------------------------------------------------------------------------------------
# Main Game Loop
#--------------------------------------------------------------------------------------------------------------
class App:
    def __init__(self):
        self.player = Player()
        self.__CLI()

    def __CLI(self):
        while True:
            # server interrupt sets player's game_trigger field to game_orientation, signalling main thread to initialise game
            if self.player.game_trigger:
                self.start_game(self.player.game_trigger)
                self.player.game_trigger = None
            # process input command
            user_input = input("Input command: ")
            if user_input == "": continue
            cmd_words = user_input.split() if re.search('\s+', user_input) else [user_input]
            cmd = cmd_words[0]
            if cmd == "help":
                print("\thelp : list all commands")
                print("\tlist : list all available players")
                print("\trequest [player] : request game with player")
                print("\texit : exit command-line interface")
                print("\thistory : print move history")
            elif cmd == "list":
                self.player.list_players()
            elif cmd == "request":
                self.player.game_request(cmd_words[1])
            elif cmd == "exit":
                self.player.leave_server()
                break
            else:
                print("Command not found. Type 'help' for list of commands.")

    def start_game(self, game_orientation):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((45*8, 45*8))
        board = GameBoard(screen, game_orientation)
        pygame.display.set_caption(self.player.player_tag)
        board.draw()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    valid_move = board.process_click_event(pygame.mouse.get_pos())
                    if valid_move:
                        self.player.send_move(valid_move)
                if self.player.opponent_next_move:
                    board.process_opponent_move(self.player.opponent_next_move)
                    if board.in_check_mate():
                        self.player.terminate_game()
                        running = False
                    self.player.opponent_next_move = None
                if self.player.end_game_trigger:
                    running = False
            pygame.display.flip()
            clock.tick(60)
        board.highlight_end_game()
        time.sleep(10)
        pygame.quit()

App()

# TODO
# FINALISE
#   checkmate
#   debug checkmate + end game
#   stylish blue board + better piece assets
#       https://berryarray.itch.io/chess-pieces-16x16-one-bit
#       https://wildlifestudios.itch.io/chess-set-pixel-art
#       https://devilsworkshop.itch.io/pixel-art-chess-asset-pack
#
#   add server event logging + shell script for testing demo
# DOCUMENT
#   create github page for chess project, use https://github.com/eliben/luz-cpu as example template