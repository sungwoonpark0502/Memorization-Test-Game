import pygame

# Initialization
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memorization Game")

# Game Loop
running = True # is the game running?
while running:
    # event loop
    for event in pygame.event.get(): # what event happened
        if event.type == pygame.QUIT: # if quit screen
            running = False # game no longer running
            
# Quit Game
pygame.quit()