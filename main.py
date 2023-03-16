import pygame
import definitions.colours as COLOURS
from definitions.game_state import GameState

from classes.pokemon import Pokemon
from views.listing import ListingView

from utils.load_data import load_pokemon_data


pygame.init()

# Create the game window
window_size = (1280, 720)
game_screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pokemon Battle')


# LOGIC AND DATA VARIABLES

# Get pokemon list
pokemon_list: list[Pokemon] = load_pokemon_data()

# Selected pokemon list
selected_pokemon: list[Pokemon] = []


# LOAD VIEWS
listingView = ListingView(pokemon_list)


# Game execution
state: list[GameState] = [GameState.LISTING]
running = True
while running:
    game_screen.fill(COLOURS.WHITE)

    # Diferents States
    match state[0]:
        case GameState.LISTING:
            # Listing View
            listingView.loop(game_screen, pokemon_list, selected_pokemon, state)

        case GameState.FILTERING:
            # Filtering View
            print('filtering')
        
        # other views

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Update window screen
    pygame.display.update()


pygame.quit()
