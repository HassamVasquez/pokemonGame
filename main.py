import pygame
import definitions.colours as COLOURS
from definitions.game_state import GameState
from views.filtering import FilteringView
from classes.pokemon_combat import PokemonCombat
from classes.pokemon import Pokemon
from views.listing import ListingView
from views.combat import Combat

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
filtered_pokemon_list: list[Pokemon] = pokemon_list.copy()

# Selected pokemon list
selected_pokemon_list: list[Pokemon] = []

#Pokemon list combat
pokemon_list_combat = []


#Test combat
pokemon_list_combat.append(PokemonCombat(pokemon_list[0].name,30,25,50,'pokemon_images/'+pokemon_list[0].image_path,pokemon_list[0].type_1, game_screen))
pokemon_list_combat.append(PokemonCombat(pokemon_list[1].name,30,25,50,'pokemon_images/'+pokemon_list[1].image_path,pokemon_list[1].type_1,game_screen))

# LOAD VIEWS
listingView = ListingView(filtered_pokemon_list)
filteringView = FilteringView()
comba = Combat(pokemon_list_combat,game_screen)


# Game execution
state: list[GameState] = [GameState.LISTING]
running = True
while running:
    game_screen.fill(COLOURS.CREAM)

    # Diferents States
    match state[0]:
        case GameState.LISTING:
            # Listing View
            listingView.loop(game_screen, filtered_pokemon_list, selected_pokemon_list, state)

        case GameState.FILTERING:
            # Filtering View
            filteringView.loop(game_screen, filtered_pokemon_list, pokemon_list, state, listingView)
          
        case GameState.SINGLE_BATTLE:
            # combat View
            comba.loop(game_screen, pokemon_list_combat, state)
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
