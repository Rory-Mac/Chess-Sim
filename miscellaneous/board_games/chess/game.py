import pygame
import os
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# initialise game
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
# load game assets
king_black = pygame.image.load(os.getcwd() + '/assets/king_black.png')
king_black = pygame.transform.scale(king_black, (100, 100))
king_white = pygame.image.load(os.getcwd() + '/assets/king_white.png')
king_white = pygame.transform.scale(king_white, (100, 100))
queen_black = pygame.image.load(os.getcwd() + '/assets/queen_black.png')
queen_black = pygame.transform.scale(queen_black, (100, 100))
queen_white = pygame.image.load(os.getcwd() + '/assets/queen_white.png')
queen_white = pygame.transform.scale(queen_white, (100, 100))
rook_black = pygame.image.load(os.getcwd() + '/assets/rook_black.png')
rook_black = pygame.transform.scale(rook_black, (100, 100))
rook_white = pygame.image.load(os.getcwd() + '/assets/rook_white.png')
rook_white = pygame.transform.scale(rook_white, (100, 100))
bishop_black = pygame.image.load(os.getcwd() + '/assets/bishop_black.png')
bishop_black = pygame.transform.scale(bishop_black, (100, 100))
bishop_white = pygame.image.load(os.getcwd() + '/assets/bishop_white.png')
bishop_white = pygame.transform.scale(bishop_white, (100, 100))
knight_black = pygame.image.load(os.getcwd() + '/assets/knight_black.png')
knight_black = pygame.transform.scale(knight_black, (100, 100))
knight_white = pygame.image.load(os.getcwd() + '/assets/knight_white.png')
knight_white = pygame.transform.scale(knight_white, (100, 100))
pawn_black = pygame.image.load(os.getcwd() + '/assets/pawn_black.png')
pawn_black = pygame.transform.scale(pawn_black, (100, 100))
pawn_white = pygame.image.load(os.getcwd() + '/assets/pawn_white.png')
pawn_white = pygame.transform.scale(pawn_white, (100, 100))
# draw overlayed board
screen.fill(BLACK)
for x in range(8):
    for y in range(8):
        pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
# draw chess pieces
screen.blit(rook_black, (0,0))
screen.blit(knight_black, (100,0))
screen.blit(bishop_black, (200,0))
screen.blit(queen_black, (300,0))
screen.blit(king_black, (400,0))
screen.blit(bishop_black, (500,0))
screen.blit(knight_black, (600,0))
screen.blit(rook_black, (700,0))
screen.blit(rook_white, (0,700))
screen.blit(knight_white, (100,700))
screen.blit(bishop_white, (200,700))
screen.blit(queen_white, (300,700))
screen.blit(king_white, (400,700))
screen.blit(bishop_white, (500,700))
screen.blit(knight_white, (600,700))
screen.blit(rook_white, (700,700))
for i in range(8):
    screen.blit(pawn_black, (i*100,100))
    screen.blit(pawn_white, (i*100,600))
# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # next frame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()