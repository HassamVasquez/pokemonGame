#Dos tipos, y n generaciones y un intervale de attack.

from pymonad.tools import curry
from pymonad.reader import Compose

@curry(3)
def select_fieldn(list_filters,l_element,d_element):

        match d_element:
            case 'type1':
                if len(types) == 0:
                    return True
                else:
                    if l_element.type1 in list_filters:return True
                    else:return False
            case 'type2':
                if len(types)==2:
                    if l_element.type2 in list_filters:return True
                    else:return False
                else:
                    return True
            case 'gen':
                if len(generations) ==0:
                    return True
                else:
                    if l_element.generation in list_filters:return True
                    else:return False
        
types,generations, = [],[]

def reduce_list(element):
    if 'type'in element: 
        types.append(element['type'])
    elif 'gen' in element: 
        generations.append(element['gen'])

def repotitionamiento(list_poke):
    y_add, x_it, y_it,  = 100, 25, 50, 
    for poke in list_poke: 
        if y_it == 650:
            y_it = 50
            if x_it == 25: x_it = 550
            else: x_it = 25
        poke.x,poke.y = x_it,y_it
        y_it += y_add
    return list_poke

def list_filtred(list_pokemons,list_filters):
    a = list(map(reduce_list,list_filters))
    filt_pokemons:list = []

    for filt in list_filters:
        if 'attack_mayor' in filt: 
            attack_mayor = filt['attack_mayor']
        elif 'attack_menor' in filt: 
            attack_menor = filt['attack_menor']

    ftype = select_fieldn(types)
    fgen = select_fieldn(generations)
    filt_pokemons = list(map(lambda x:x,filter(lambda y:((ftype(y,'type1')==True and ftype(y,'type2')==True) and (fgen(y,'gen') == True ) and (attack_menor<=int(y.attack) and int(y.attack)<=attack_mayor) ),list_pokemons)))
    types.clear(),generations.clear()
    attack_mayor,attack_menor = 0,0
    return repotitionamiento(filt_pokemons)

