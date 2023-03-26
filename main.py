import pygame
import definitions.colours as COLOURS
from random import randint
from definitions.game_state import GameState
from definitions.team_battle import TeamBattle
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


#Select rival single battle

flag = bool
flag = True
flagTeam : list[TeamBattle] = [TeamBattle.DEFINITIONS]
points = [0,0]

i = 0
numPokes = 3
# LOAD VIEWS
listingView = ListingView(filtered_pokemon_list)
filteringView = FilteringView()



# Game execution
state: list[GameState] = [GameState.LISTING]
running = True
while running:
    game_screen.fill(COLOURS.CREAM)

    # Diferents States
    match state[0]:
        case GameState.LISTING:
            # Listing View
            flag = True
            flagTeam[0] = TeamBattle.DEFINITIONS
            numPokes = 4
            i, points[0], points[1] = 0, 0, 0
            listingView.loop(game_screen, filtered_pokemon_list, selected_pokemon_list, state)

        case GameState.FILTERING:
            # Filtering View
            filteringView.loop(game_screen, filtered_pokemon_list, pokemon_list, state, listingView)
            

        case GameState.SINGLE_BATTLE:
            # combat View
            
            if flag == True:
                ran = randint(1, 720)
                pokemon_list_combat.insert(0,PokemonCombat(selected_pokemon_list[0].name,30,25,50,'pokemon_images/'+selected_pokemon_list[0].image_path,selected_pokemon_list[0].type_1, game_screen))
                pokemon_list_combat.insert(1,PokemonCombat(pokemon_list[ran].name,30,25,50,'pokemon_images/'+pokemon_list[ran].image_path,pokemon_list[ran].type_1,game_screen))
                comb = Combat(pokemon_list_combat,game_screen)
                flag = 0
            else:
                comb.loop(game_screen, state,flagTeam,1)

        case GameState.TEAM_BATTLE:
            # combat View
            match flagTeam[0]:

                case TeamBattle.DEFINITIONS:
                    ran = randint(1, 720)
                    pokemon_list_combat.insert(0,PokemonCombat(selected_pokemon_list[i].name,30,25,50,'pokemon_images/'+selected_pokemon_list[i].image_path,selected_pokemon_list[i].type_1, game_screen))
                    pokemon_list_combat.insert(1,PokemonCombat(pokemon_list[ran].name,30,25,50,'pokemon_images/'+pokemon_list[ran].image_path,pokemon_list[ran].type_1,game_screen))
                    comb = Combat(pokemon_list_combat,game_screen)
                    flagTeam[0] = TeamBattle.BATTLE
                    i  = i + 1
                    numPokes = numPokes - 1

                case TeamBattle.BATTLE:
                    comb.loop(game_screen, state, flagTeam, numPokes,points)
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
