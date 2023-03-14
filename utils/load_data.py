from os import listdir
from csv import reader as csv_reader


def read_pokemons_data():
    result = []
    with open('pokemon.csv') as pokemon_csv:
        pokemons = csv_reader(pokemon_csv, delimiter = ',')
        next(pokemons)
        result = [{
            'id': pokemon[0],
            'name': pokemon[1],
            'type_1': pokemon[2],
            'type_2': pokemon[3],
            'hp': pokemon[5],
            'attack': pokemon[6],
            'generation': pokemon[11]
        } for pokemon in pokemons]

    return result

def load_pokemon_data():
	# get images name list
    pokemon_images_list = sorted(listdir('pokemon_jpg'), key=lambda x: int(x.split('.')[0]))

	# get info pokemon list
    pokemon_info_list = read_pokemons_data()

    # Create Pokemon objects list

    return pokemon_info_list

print(load_pokemon_data())