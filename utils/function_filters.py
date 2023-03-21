def filter_type(list_type):
    def func_pokemon(pokemon):
        match len(list_type):
            case 1:
                if(pokemon.type_1 in list_type): return True
                else : return False
            case 2:
                if(pokemon.type_1 in list_type and pokemon.type_2 in list_type): return True
                else: return False
            case _:
                return True
    return func_pokemon

def filter_gen(list_gen):
    def func_pokemon(pokemon):
        if(pokemon.generation in list_gen or not list_gen): return True
        else : return False
    return func_pokemon
    
def list_filtred(list_pokemons, dict_filters):
    if dict_filters['type'] or dict_filters['gen']:
        f_type, f_gen = filter_type(dict_filters['type']), filter_type(dict_filters['gen'])
        filtred = list(map(lambda x:x, filter(lambda y:(f_type(y) and f_gen(y)), list_pokemons)))
        return filtred
    else:
        return list_pokemons
