import pygame

# showing the start screen
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    
# Initialization
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memorization Game")

# Start Button
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

# Color (RGB)
BLACK = (0,0,0)
WHITE = (255,255,255)

# Game Loop
running = True # is the game running?
while running:
    # event loop
    for event in pygame.event.get(): # what event happened
        if event.type == pygame.QUIT: # if quit screen
            running = False # game no longer running
            
    # screen color to black
    screen.fill(BLACK)
    
    # show start screen
    display_start_screen()
    
    # update screen
    pygame.display.update()
    
# Quit Game
pygame.quit()