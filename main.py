import pygame
import definitions.colours as COLOURS
from definitions.game_state import GameState
from views.filtering import FilteringView
from classes.pokemon import Pokemon
from views.listing import ListingView

from utils.load_data import load_pokemon_data


pygame.init()


# Create the game window
window_size = (1280, 720)
game_screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pokemon Battle')
clock = pygame.time.Clock()


# LOGIC AND DATA VARIABLES

# Get pokemon list
pokemon_list: list[Pokemon] = load_pokemon_data()
pokemon_list_filtered=[]

# Selected pokemon list
selected_pokemon_list: list[Pokemon] = []

# LOAD VIEWS
listingView = ListingView(pokemon_list)
filteringView=FilteringView()


# Game execution
state: list[GameState] = [GameState.LISTING]
running = True
while running:
    game_screen.fill(COLOURS.WHITE)

    # Diferents States
    match state[0]:
        case GameState.LISTING:
            # Listing View
            listingView.loop(game_screen, pokemon_list, selected_pokemon_list, state)

        case GameState.FILTERING:
            # Filtering View
            filteringView.loop(game_screen,pokemon_list_filtered,pokemon_list)
            
        
        # other views

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Update window screen
    pygame.display.update()

    # FPS
    clock.tick(60)

pygame.quit()
