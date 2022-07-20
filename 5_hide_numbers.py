from cgitb import text
import pygame
from random import*

# settings for level
def setup(level):
    # how many numbers are we going to show
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) # if over 20, set as 20
    
    # set numbers at screen as grid
    shuffle_grid(number_count)
    
# Shuffling Numbers
def shuffle_grid(number_count):
    rows = 5
    columns = 9
    
    cell_size = 130 # width and height size of grid cell
    button_size = 120 # button size
    screen_left_margin = 55
    screen_top_margin = 20
    
    
    # [[0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0]]
    grid = [[0 for col in range(columns)] for row in range(rows)]
    
    number = 1 # start with 1 to number_count
    while number <= number_count:
        row_idx = randrange(0, rows) # random num from 0 ~ 4
        col_idx = randrange(0, columns) # random num from 0 ~ 8

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number # set number
            number += 1
            
            # get x & y coordinate with the current grid cell location
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)
            
            # making number button
            button = pygame.Rect(0,0,button_size, button_size)
            button.center = (center_x, center_y)
            
            number_buttons.append(button)
            
    # check randomly setted numbers
    print(grid)
    
# showing the start screen
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
  
# Showing Game Screen  
def display_game_screen():
    for idx, rect in enumerate(number_buttons, start = 1):
        if hidden:
            # drawing rectangle button
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # number text
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)

# check button correspondent to pos   
def check_buttons(pos):
    global start
    
    if start: # if game started?
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        
def check_number_buttons(pos):
    global hidden
    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]: # click right button
                print("Correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True # hide the number
            else:
                print("Wrong")
            break
        
# Initialization
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memorization Game")
game_font = pygame.font.Font(None, 120) # font

# Start Button
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120, screen_height - 120)

# Color (RGB)
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (50,50,50)

# List of Number Buttons
number_buttons = [] # buttons that the user has to click

# Game Start or Not
start = False

# number hidden or not
hidden = False

# Using Game Level Setting Function before the Game
setup(1)

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