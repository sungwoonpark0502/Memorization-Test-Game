import pygame

# showing the start screen
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
  
# Showing Game Screen  
def display_game_screen():
    print("Game Start")

# check button correspondent to pos   
def check_buttons(pos):
    global start
    if start_button.collidepoint(pos):
        start = True
        
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

# Game Start or Not
start = False


# Game Loop
running = True # is the game running?
while running:
    click_pos = None
    # event loop
    for event in pygame.event.get(): # what event happened
        if event.type == pygame.QUIT: # if quit screen
            running = False # game no longer running
        elif event.type == pygame.MOUSEBUTTONUP: # when user clicked the mouse
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
            
    # screen color to black
    screen.fill(BLACK)
    
    if start:
        display_game_screen() # show game screen
    else:
        display_start_screen() # show start screen

    # if user clicked coordinate is valid
    if click_pos:
        check_buttons(click_pos)
        
    
    # update screen
    pygame.display.update()
    
# Quit Game
pygame.quit()