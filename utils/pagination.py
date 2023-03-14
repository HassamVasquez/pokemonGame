from classes.list_card import ListCard
from classes.pokemon import Pokemon

# X and Y position for cards
X_VALUES = [160, 480, 800, 1120]
Y_VALUES = [140, 320, 500]


def create_list_card(x_values: list[int], y_values: list[int], pokemon_i:tuple[int, Pokemon]) -> ListCard:
    i, pokemon = pokemon_i
    return ListCard(x_values[i - (int(i / 4) * 4)], y_values[int(i / 4)], pokemon)

# Update pokemon page list
def get_paged_card_list(page: int, pokemon_list: list[Pokemon]) -> list[ListCard]:
    pokemon_paged_list = pokemon_list[page * 12: page * 12 + 12]

    # Update card's list pokemon
    return [create_list_card(X_VALUES, Y_VALUES, pokemon) for pokemon in enumerate(pokemon_paged_list)]

