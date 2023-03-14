import pygame
import definitions.colours as COLOURS

from classes.action_button import ActionButton
from classes.list_card import ListCard
from classes.pokemon import Pokemon

from utils.load_data import load_pokemon_data


pygame.init()

# Create the game window
window_size = (1280, 720)
game_screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pokemon Battle')

# Get pokemon
pokemon_list: list[Pokemon] = load_pokemon_data()

# Pokemon pagination
page = 0
def paginate_pokemon_list(page: int, pokemon_list: list[Pokemon]) -> list[Pokemon]:
	return pokemon_list[page * 12: page * 12 + 12]

# Pokemon page list
pokemon_page_list: list[Pokemon] = paginate_pokemon_list(page, pokemon_list)

# Font
font = pygame.font.SysFont('consolas', 60, bold=True)

# Load button image
button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()

# Create button instances
back_button = ActionButton(300, 670, button_background, 'BACK', hover_scale=1.08)
filter_button = ActionButton(640, 670, button_background, 'FILTER', hover_scale=1.08)
next_button = ActionButton(980, 670, button_background, 'NEXT', hover_scale=1.08)

# Create cards
cards_list: list[ListCard] = [
    ListCard(160, 160, pokemon_page_list[0]),
    ListCard(480, 160, pokemon_page_list[1]),
    ListCard(800, 160, pokemon_page_list[2]),
    ListCard(1120, 160, pokemon_page_list[3]),
    ListCard(160, 340, pokemon_page_list[4]),
    ListCard(480, 340, pokemon_page_list[5]),
    ListCard(800, 340, pokemon_page_list[6]),
    ListCard(1120, 340, pokemon_page_list[7]),
    ListCard(160, 520, pokemon_page_list[8]),
    ListCard(480, 520, pokemon_page_list[9]),
    ListCard(800, 520, pokemon_page_list[10]),
    ListCard(1120, 520, pokemon_page_list[11])
]


# Update pokemon page list
def update_page_list():
    pokemon_page_list = paginate_pokemon_list(page, pokemon_list)

    # Update card's list pokemon
    for i, pokemon in enumerate(pokemon_page_list):
        cards_list[i].update_pokemon(pokemon)


# Game execution
running = True
while running:
    game_screen.fill(COLOURS.WHITE)

    # Title
    title = font.render('POKEMON LIST', True, COLOURS.BLACK)
    game_screen.blit(title, (440, 20))

    # Back button action
    if back_button.draw(game_screen):
        page -= 1
        update_page_list()

    # Next button action
    if next_button.draw(game_screen):
        page += 1
        update_page_list()

    # Filter button action
    filter_button.draw(game_screen)

    # Pokemon page list
    clickedCards = [card.draw(game_screen) for card in cards_list]
    # Clicked card
    if any(clickedCards):
        clickedCard = clickedCards.index(True)
        print(f'Se clickeo card {clickedCard}')


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()


pygame.quit()
