import time
import pygame,sys,csv,os,random
from pygame.locals import *
from natsort import natsorted,ns
from pymonad.reader import Compose
import combate as cb
import filtros as filters
import filters_functions as ffunctions

pygame.init()

# create the game window
game_width, game_height = 1000, 800
size = (game_width, game_height)
game_screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon Battle')
black,gold,grey,green,red,white = (0, 0, 0),(218, 165, 32),(200, 200, 200),(0, 200, 0),(200, 0, 0),(255, 255, 255)
#back_image,next_image = pygame.image.load('back.jpg'),pygame.image.load('next.jpg').convert_alpha()



class Pokemon(pygame.sprite.Sprite):
    def __init__(self, x, y, dat_pok, route_image):
        self.head = ['#','Name','Type 1','Type 2','Total','HP','Attack','Defense','Sp. Atk','Sp. Def','Speed','Generation','Legendary']
        pygame.sprite.Sprite.__init__(self)
        
        #Posición y ruta de la imagen.
        self.x,self.y,self.route = x,y,route_image

        #Pokemon information
        self.name,self.type1,self.type2 = dat_pok[self.head.index('Name')],dat_pok[self.head.index('Type 1')],dat_pok[self.head.index('Type 2')]
        self.total,self.HP,self.attack = dat_pok[self.head.index('Total')],dat_pok[self.head.index('HP')],dat_pok[self.head.index('Attack')]
        self.defense,self.sp_atk,self.sp_def = dat_pok[self.head.index('Defense')],dat_pok[self.head.index('Sp. Atk')],dat_pok[self.head.index('Sp. Def')]
        self.speed,self.generation,self.legendary = dat_pok[self.head.index('Speed')],dat_pok[self.head.index('Generation')],dat_pok[self.head.index('Legendary')]

        self.size = 100
        self.set_sprite()
    
    def set_sprite(self):
        self.image = pygame.image.load(self.route)
        scale = self.size/self.image.get_width()
        new_width,new_height = self.image.get_width() * scale,self.image.get_height()* scale
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
    
    def draw(self,alpha = 255):
        #x cada self.size pixeles
        sprite, transparency= self.image.copy(),(255,255,255,alpha)
        sprite.fill(transparency,None,pygame.BLEND_RGB_MULT)
        game_screen.blit(sprite,(self.x,self.y))
    
    def draw_information(self,x,y):
        display_mesage(self.name,x,y)
        display_mesage(self.type1,x,y+20)
        display_mesage(self.type2,x,y+40)
        display_mesage(self.attack,x,y+60)
    
    def get_rect(self):
        return Rect(self.x,self.y,self.image.get_width(),self.image.get_height())

def display_mesage(message,x,y):
    #y cada 25 pixeles
    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    text = font.render(message, True, black)
    text_rect = text.get_rect()
    text_rect.x,text_rect.y = x, y
    game_screen.blit(text, text_rect)

def read_images():
    with os.scandir('pokemon_jpg') as images:
        images = natsorted(images,alg = ns.PATH|ns.IGNORECASE)
        yield from images
 
def read_pokemons():
    with open('pokemon.csv') as pokemon_csv:
        pokemons = csv.reader(pokemon_csv, delimiter = ',')
        next(pokemons)
        yield from pokemons

def zip_pokemons()->list:
    y_add, x_it, y_it, list_pokemons = 100, 25, 50, []

    for image,pokemon in zip(read_images(),read_pokemons()):  
        if y_it == 650:
            y_it = 50
            if x_it == 25: x_it = 550
            else: x_it = 25
        list_pokemons.append(Pokemon(x_it,y_it,pokemon,'pokemon_jpg/'+image.name))
        y_it += y_add
    
    return list_pokemons

def divition_pokemons(n = 0,list_poke = [],band_filter = False):
    l_pokemos = zip_pokemons()
    if  band_filter == False:
        l_pokemos = zip_pokemons()
        return l_pokemos[n:n+12],n+12
    else:
        l_pokemos = list_poke
        return l_pokemos[n:n+12],n+12
    

def print_pokemons(pokemons)-> list:
    for pokemon in pokemons:
        pokemon.draw()
        pokemon.draw_information(pokemon.x+120,pokemon.y+25)
    return pokemons

def draw_contorno(pokemons):
    mouse_cursor = pygame.mouse.get_pos()
    for pokemon in pokemons:
        if pokemon.get_rect().collidepoint(mouse_cursor):
            pygame.draw.rect(game_screen,black,pokemon.get_rect(),2)
    
    pygame.display.update()

def create_button(width, height, left, top, text_cx, text_cy, label):
    # position of the mouse cursor
    mouse_cursor = pygame.mouse.get_pos()
    button = Rect(left, top, width, height)
    # highlight the button if mouse is pointing to it
    if button.collidepoint(mouse_cursor):
        pygame.draw.rect(game_screen, gold, button)
    else:
        pygame.draw.rect(game_screen, white, button)
    # add the label to the button
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'{label}', True, black)
    text_rect = text.get_rect(center=(text_cx, text_cy))
    game_screen.blit(text, text_rect) 
    return button
   
def list_main(list_filters = []):
    pokemons_csv,pokemons_filter = [],[]
    band_filter = False
    pokemons = []
    if  len(list_filters) == 0:
        pokemons_csv.clear()
        pokemons_csv,n = divition_pokemons()
        pokemons = pokemons_csv
    else:
        band_filter = True
        pokemons_filter.clear()
        pokemons_filter = ffunctions.list_filtred(zip_pokemons(),list_filters)
        pokemons,n = divition_pokemons(0,pokemons_filter,band_filter)      
        

    while True:
        game_screen.fill(white)
        next_button = create_button(140, 50, 837, 708, 900, 730,'Next')
        back_button = create_button(140, 50, 35, 708, 98, 730,'Back')
        filter_button = create_button(140, 50, 300, 708, 370, 730,'Filter')

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
            if event.type == MOUSEBUTTONDOWN:
                # coordinates of the mouse click
                mouse_click = event.pos
                if next_button.collidepoint(mouse_click):
                    if pokemons:
                        if  len(list_filters) != 0: #aqui quite if  len(list_filters) != 0
                            pokemons,n = divition_pokemons(n,pokemons_filter,band_filter)
                        else:
                            pokemons,n = divition_pokemons(n,pokemons_csv,band_filter)
                            
                    
                if back_button.collidepoint(mouse_click):
                    if n > 12:
                        if  len(list_filters) != 0: 
                            pokemons,n = divition_pokemons(n-24,pokemons_filter,band_filter)
                        else:
                            pokemons,n = divition_pokemons(n-24,pokemons_csv,band_filter)
                        
                if filter_button.collidepoint(mouse_click):
                    filters.show_filters()
                for count,pokemon in enumerate(pokemons):
                    if pokemon.get_rect().collidepoint(mouse_click):
                        x = (random.randint(1, 12))
                        pokemon_rival = cb.PokemonBattle(pokemons[x].name,30,25,50,pokemons[x].route,pokemons[x].type1)
                        pokemon_player = cb.PokemonBattle(pokemon.name,30,25,50,pokemon.route,pokemon.type1)
                        pokemonBattle = [pokemon_player, pokemon_rival]
                        #time.sleep(1)
                        cb.battle(pokemonBattle)

        l_poke = Compose(print_pokemons).then(draw_contorno)
        l_poke(pokemons)
        
        pygame.display.update()
if __name__ == '__main__':
    list_main()
    #filters.muestra_filtros()
