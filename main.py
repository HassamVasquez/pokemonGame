import pygame
from classes.button import Button
import definitions.colours as COLOURS
from classes.list_card import ListCard


pygame.init()

# Create the game window
window_size = (1280, 720)
game_screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pokemon Battle')

# Font
font = pygame.font.SysFont('consolas', 60, bold=True)

# Load button image
button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()

# Create button instances
back_button = Button(300, 670, button_background, 'BACK', hover_scale=1.08)
filter_button = Button(640, 670, button_background, 'FILTER', hover_scale=1.08)
next_button = Button(980, 670, button_background, 'NEXT', hover_scale=1.08)

# Create card
card = ListCard(160, 160)
card2 = ListCard(480, 160)
card3 = ListCard(800, 160)
card4 = ListCard(1120, 160)
card5 = ListCard(160, 340)
card6 = ListCard(480, 340)
card7 = ListCard(800, 340)
card8 = ListCard(1120, 340)
card9 = ListCard(160, 520)
card10 = ListCard(480, 520)
card11 = ListCard(800, 520)
card12 = ListCard(1120, 520)


# Game execution
running = True
while running:
    game_screen.fill(COLOURS.WHITE)

    # Title
    title = font.render('POKEMON LIST', True, COLOURS.BLACK)
    game_screen.blit(title, (440, 20))

    # Back button action
    back_button.draw(game_screen)

    # Next button action
    next_button.draw(game_screen)

    # Filter button action
    filter_button.draw(game_screen)

    # Card
    card.draw(game_screen)
    card2.draw(game_screen)
    card3.draw(game_screen)
    card4.draw(game_screen)
    card5.draw(game_screen)
    card6.draw(game_screen)
    card7.draw(game_screen)
    card8.draw(game_screen)
    card9.draw(game_screen)
    card10.draw(game_screen)
    card11.draw(game_screen)
    card12.draw(game_screen)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()


pygame.quit()
