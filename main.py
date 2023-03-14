import pygame
import definitions.colours as COLOURS
from math import ceil

from classes.action_button import ActionButton
from classes.list_card import ListCard
from classes.pokemon import Pokemon

from utils.load_data import load_pokemon_data
from utils.pagination import get_paged_card_list


pygame.init()

# Create the game window
window_size = (1280, 720)
game_screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pokemon Battle')


# LOGIC AND DATA VARIABLES

# Get pokemon
pokemon_list: list[Pokemon] = load_pokemon_data()

# Pagination page
page = 0
total_pages = ceil(len(pokemon_list) / 12)


# VISUAL ELEMENTS

# Title
title_font = pygame.font.SysFont('consolas', 60, bold=True)
title = title_font.render('POKEMON LIST', True, COLOURS.BLACK)

# Number page
number_page_font = pygame.font.SysFont('consolas', 30, bold=True)

# Load button image
button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()

# Create button instances
back_button = ActionButton(300, 680, button_background, 'BACK', hover_scale=1.08)
filter_button = ActionButton(640, 680, button_background, 'FILTER', hover_scale=1.08)
next_button = ActionButton(980, 680, button_background, 'NEXT', hover_scale=1.08)


# Create initial cards
cards_list: list[ListCard] = get_paged_card_list(page, pokemon_list)

# Game execution
running = True
while running:
    game_screen.fill(COLOURS.WHITE)

    # Title
    game_screen.blit(title, (440, 5))

    # Number Page
    number_page = number_page_font.render(f'Page {page + 1} of {total_pages} pages', True, COLOURS.BLACK)
    game_screen.blit(number_page, (480, 600))

    # Back button action
    if back_button.draw(game_screen) and page > 0:
        page -= 1
        cards_list = get_paged_card_list(page, pokemon_list)

    # Next button action
    if next_button.draw(game_screen) and page < total_pages - 1:
        page += 1
        cards_list = get_paged_card_list(page, pokemon_list)

    # Filter button action
    filter_button.draw(game_screen)

    # Pokemon paged list
    clickedCards = [card.draw(game_screen) for card in cards_list]
    # Clicked card
    if any(clickedCards):
        clickedCard = clickedCards.index(True)
        print(f'Se clickeo card {clickedCard}')


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Update window screen
    pygame.display.update()


pygame.quit()
