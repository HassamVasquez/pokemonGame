from csv import reader as csv_reader
from operator import itemgetter
from classes.pokemon import Pokemon


def read_pokemons_data() -> list[dict]:
    result = []
    with open('pokemon.csv') as pokemon_csv:
        pokemons = csv_reader(pokemon_csv, delimiter = ',')
        header = next(pokemons)
        getId = itemgetter(header.index('#'))
        getName = itemgetter(header.index('Name'))
        getType1 = itemgetter(header.index('Type 1'))
        getType2 = itemgetter(header.index('Type 2'))
        getHP = itemgetter(header.index('HP'))
        getAttack = itemgetter(header.index('Attack'))
        getGeneration = itemgetter(header.index('Generation'))

        result = [{
            'id': int(getId(pokemon)),
            'name': getName(pokemon),
            'type_1': getType1(pokemon),
            'type_2': getType2(pokemon),
            'hp': int(getHP(pokemon)),
            'attack': int(getAttack(pokemon)),
            'generation': int(getGeneration(pokemon))
        } for pokemon in pokemons]

    return result

def load_pokemon_data() -> list[Pokemon]:
	# get info pokemon list
    pokemon_info_list = read_pokemons_data()

    # Create Pokemon objects list
    pokemon_objects_list = [Pokemon(pokemon) for pokemon in pokemon_info_list]

    return pokemon_objects_list
