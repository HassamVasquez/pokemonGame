import pygame
from pygame.locals import *
import time
import math
import random
import listado as l
from functools import partial
from definitions import colours as COLOURS
pygame.init()

game_width, game_height = 1000, 750
size = (game_width, game_height)
game_screen = pygame.display.set_mode(size)


mov_plant = [{'name': 'Planta feroz', 'atack': 45},{'name': 'Latigo cepa', 'atack': 20},{'name': 'Hoja aguda ', 'atack': 30},{'name': 'Bomba germen ', 'atack': 10}]
mov_fuego = [{'name': 'Sofoco', 'atack': 30},{'name': 'Anillo igneo ', 'atack': 45},{'name': 'Nitrocarga', 'atack': 40},{'name': 'Puño fuego ', 'atack': 10}]
mov_tierra = [{'name': 'Terremoto', 'atack': 45},{'name': 'Tierra viva', 'atack': 40},{'name': 'Bomba fango', 'atack': 30},{'name': 'Disparo lodo', 'atack': 10}]
mov_roca = [{'name': 'Avalancha', 'atack': 45},{'name': 'Poder pasado', 'atack': 40},{'name': 'Lanza rocas', 'atack': 30},{'name': 'Pedrada', 'atack': 10}]
mov_siniestro = [{'name': 'Triturar', 'atack': 45},{'name': 'Mordisco', 'atack': 40},{'name': 'Juego sucio', 'atack': 30},{'name': 'Alarido', 'atack': 10}]
mov_fantasma = [{'name': 'Bola sombra', 'atack': 100},{'name': 'Puño sombra', 'atack': 40},{'name': 'Hueso sombrio', 'atack': 30},{'name': 'Garra umbria', 'atack': 10}]
mov_lucha = [{'name': 'Onda certera', 'atack': 120},{'name': 'Puño dinamico', 'atack': 40},{'name': 'Puño incremento', 'atack': 15},{'name': 'Contraataque', 'atack': 5}]
mov_electrico = [{'name': 'Voltio cruel', 'atack': 45},{'name': 'Impactrueno', 'atack': 40},{'name': 'Puño trueno', 'atack': 30},{'name': 'Chispazo', 'atack': 10}]
mov_hada= [{'name': 'Carantoña', 'atack': 45},{'name': 'Brillo magico', 'atack': 40},{'name': 'Encanto', 'atack': 30},{'name': 'Fuerza lunar', 'atack': 10}]
mov_psiquico = [{'name': 'Onda mental', 'atack': 45},{'name': 'Sincroruido', 'atack': 40},{'name': 'Confusion', 'atack': 30},{'name': 'Psiquico', 'atack': 10}]
mov_veneno = [{'name': 'Veneno X', 'atack': 45},{'name': 'Veneno Y', 'atack': 40},{'name': 'Bomba acida', 'atack': 30},{'name': 'Picadura', 'atack': 10}]
mov_acero = [{'name': 'Puño meteorico', 'atack': 45},{'name': 'Rayo luz', 'atack': 40},{'name': 'Foco resplandor', 'atack': 30},{'name': 'Disparo espejo', 'atack': 10}]
mov_normal = [{'name': 'Hiperrayo', 'atack': 45},{'name': 'Golpe cuerpo', 'atack': 40},{'name': 'Destructor', 'atack': 30},{'name': 'Ultima baza', 'atack': 10}]
mov_volador = [{'name': 'Ataque aereo', 'atack': 45},{'name': 'Pajaro osado', 'atack': 40},{'name': 'Vendaval', 'atack': 30},{'name': 'Terreneitor', 'atack': 10}]
mov_bicho = [{'name': 'Picadura', 'atack': 45},{'name': 'Plancha', 'atack': 40},{'name': 'Zuumbido', 'atack': 30},{'name': 'Acoso', 'atack': 10}]
mov_agua = [{'name': 'Hidrobombda', 'atack': 45},{'name': 'Hidropulso', 'atack': 40},{'name': 'Acua cola', 'atack': 30},{'name': 'Pistola agua', 'atack': 10}]
mov_hielo = [{'name': 'Meterobola', 'atack': 45},{'name': 'Ventisca', 'atack': 40},{'name': 'Rayo hielo', 'atack': 30},{'name': 'Puño hielo', 'atack': 10}]
mov_dragon = [{'name': 'Enfado', 'atack': 100},{'name': 'Cometa draco', 'atack': 40},{'name': 'Garra dragon', 'atack': 30},{'name': 'Cola dragon', 'atack': 10}]

#Pokemons
class PokemonBattle(pygame.sprite.Sprite):
    def __init__(self, name, level, x, y, route,type):
        pygame.sprite.Sprite.__init__(self)
        self.name,self.level,self.x,self.y,self.route= name,level,x,y,route
        self.max_hp = 100 + level
        self.current_hp = 130
        self.type = type
        self.size = 150
        self.num_potions = 3
        self.set_sprite()
    
    def set_sprite(self):
        self.image = pygame.image.load(self.route)
        scale = self.size/self.image.get_width()
        new_width,new_height = self.image.get_width() * scale,self.image.get_height()* scale
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
    
    def draw(self,alpha = 255):
        sprite, transparency= self.image.copy(),(255,255,255,alpha)
        sprite.fill(transparency,None,pygame.BLEND_RGB_MULT)
        game_screen.blit(sprite,(self.x,self.y))
    def draw_hp(self):
        
        bar_scale = 200 // self.max_hp
        for i in range(self.max_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(game_screen, COLOURS.RED, bar)
            
        for i in range(self.current_hp):
            bar = (self.hp_x + bar_scale * i, self.hp_y, bar_scale, 20)
            pygame.draw.rect(game_screen, COLOURS.GREEN, bar)
            
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'HP: {self.current_hp} / {self.max_hp}', True, COLOURS.BLACK)
        text_rect = text.get_rect()
        text_rect.x = self.hp_x
        text_rect.y = self.hp_y + 30
        game_screen.blit(text, text_rect)
    
    def set_moves(self):
        self.moves = []
        if self.name == 'Magikarp': self.moves = [{'name': 'Salpicar ', 'atack': 1}]
        elif self.type == 'Grass': self.moves = mov_plant  
        elif self.type == 'Bug': self.moves = mov_bicho
        elif self.type == 'Dark': self.moves = mov_siniestro
        elif self.type == 'Psychic': self.moves = mov_psiquico
        elif self.type == 'Steel': self.moves = mov_acero
        elif self.type == 'Fairy': self.moves = mov_hada
        elif self.type == 'Ice': self.moves = mov_hielo
        elif self.type == 'Normal': self.moves = mov_normal
        elif self.type == 'Ghost': self.moves = mov_fantasma
        elif self.type == 'Electric': self.moves = mov_electrico
        elif self.type == 'Water': self.moves = mov_agua
        elif self.type == 'Dragon': self.moves = mov_dragon
        elif self.type == 'Rock': self.moves = mov_roca
        elif self.type == 'Ground':self.moves = mov_tierra
        elif self.type == 'Fire':self.moves = mov_fuego
        elif self.type == 'Fighting': self.moves = mov_lucha
        elif self.type == 'Poison': self.moves = mov_veneno
        elif self.type == 'Flying': self.moves = mov_volador

        if len(self.moves) > 4:
            self.moves = random.sample(self.moves, 4)

    def perform_attack(self, rival, move,me,band):
        if band == 1:
            drawBatlle(me,rival)
        elif band ==0 :
            drawBatlle(rival,me)
        name = move['name']
        display_message(f'{self.name} used {name}')
        
        
        damage = move['atack']

        damage = math.floor(damage)
        
        rival.take_damage(damage)
        
    def take_damage(self, damage):
        
        self.current_hp -= damage
        
        if self.current_hp < 0:
            self.current_hp = 0
    
    def use_potion(self):
        
        if self.num_potions > 0:
            
            self.current_hp += 30
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp
                
            self.num_potions -= 1



def changeTamDisplay(x,y):
    game_width = x
    game_height = y
    size = (game_width, game_height)
    game = pygame.display.set_mode(size)
    pygame.display.set_caption('Pokemon Battle')

def display_message(message):
    pygame.draw.rect(game_screen, COLOURS.WHITE, (10, 350, 480, 140))
    pygame.draw.rect(game_screen, COLOURS.BLACK, (10, 350, 480, 140), 3)
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(message, True, COLOURS.BLACK)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410
    game_screen.blit(text, text_rect)
    pygame.display.update()

def battle(pokes):
    pygame.display.set_caption('Pokemon Battle')
    changeTamDisplay(500,500)
    cD = partial(changeTamDisplay,1000)
    game_status = 'BattlePokemon'
    rival_pokemon = pokes[1]
    player_pokemon = pokes[0]
    while game_status != 'quit':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cD(800)
                l.list_main()
            game_screen.fill(COLOURS.WHITE)
            if event.type == KEYDOWN:

                if event.key == K_y:
                    player_pokemon.current_hp = 130
                    rival_pokemon.current_hp = 130
                    game_status = 'BattlePokemon'
                elif event.key == K_n:
                    cD(800)
                    l.list_main()

            if event.type == MOUSEBUTTONDOWN:

                mouse_click = event.pos

                if game_status == 'player turn':
                    drawBatlle(player_pokemon,rival_pokemon)
                    if fight_button.collidepoint(mouse_click):
                        game_status = 'player move'

                    if potion_button.collidepoint(mouse_click):
                        
                        if player_pokemon.num_potions == 0:
                            display_message('No more potions left')
                            time.sleep(1)
                            game_status = 'player move'
                        else:
                            player_pokemon.use_potion()
                            display_message(f'{player_pokemon.name} used potion')
                            time.sleep(1)
                            game_status = 'rival turn'
                    pygame.display.update()

                elif game_status == 'player move':
                    
                    for i in range(len(move_buttons)):
                        button = move_buttons[i]
                        
                        if button.collidepoint(mouse_click):
                            move = player_pokemon.moves[i]
                            player_pokemon.perform_attack(rival_pokemon, move,player_pokemon,1)
                            
                            if rival_pokemon.current_hp == 0:
                                game_status = 'fainted'
                            else:
                                game_status = 'rival turn'
                    pygame.display.update()
            
        if game_status == 'BattlePokemon':
            
            player_pokemon.x = 0
            player_pokemon.y = 175
            rival_pokemon.x = 300
            rival_pokemon.y = -10
            alpha = 0
            while alpha < 255:
                game_screen.fill(COLOURS.WHITE)
                rival_pokemon.draw(alpha)
                display_message(f'El rival eligio a  {rival_pokemon.name}!')
                alpha += .4
                
                pygame.display.update()
            time.sleep(1)
            alpha = 0
            while alpha < 255:
                game_screen.fill(COLOURS.WHITE)
                rival_pokemon.draw()
                player_pokemon.draw(alpha)
                display_message(f'Ve {player_pokemon.name}!')
                alpha += .4
                
                pygame.display.update()
            time.sleep(1)
            player_pokemon.hp_x = 275
            player_pokemon.hp_y = 250
            rival_pokemon.hp_x = 50
            rival_pokemon.hp_y = 50

            player_pokemon.draw_hp()
            rival_pokemon.draw_hp()
            player_pokemon.set_moves()
            rival_pokemon.set_moves()

            game_status = 'player turn'

        if game_status == 'player turn':
            
            drawBatlle(player_pokemon,rival_pokemon)

            fight_button = create_button(240, 140, 10, 350, 130, 412, 'Fight')
            potion_button = create_button(240, 140, 250, 350, 370, 412, f'Use Potion ({2})')

            pygame.draw.rect(game_screen, COLOURS.BLACK, (10, 350, 480, 140), 3)
            
            pygame.display.update()

        if game_status == 'player move':
            
            drawBatlle(player_pokemon,rival_pokemon)
            
            move_buttons = []
            for i in range(len(player_pokemon.moves)):
                move = player_pokemon.moves[i]
                button_width = 240
                button_height = 70
                left = 10 + i % 2 * button_width
                top = 350 + i // 2 * button_height
                text_center_x = left + 120
                text_center_y = top + 35
                button = create_button(button_width, button_height, left, top, text_center_x, text_center_y, move['name'].capitalize())
                move_buttons.append(button)
                
            pygame.draw.rect(game_screen, COLOURS.BLACK, (10, 350, 480, 140), 3)
            
            pygame.display.update()
            
        if game_status == 'rival turn':
            
            drawBatlle(player_pokemon,rival_pokemon)
            
            display_message('')
            time.sleep(1)
            move = random.choice(rival_pokemon.moves)
            rival_pokemon.perform_attack(player_pokemon, move, rival_pokemon,0)
            
            if player_pokemon.current_hp == 0:
                game_status = 'fainted'
            else:
                game_status = 'player turn'

        if game_status == 'fainted':
            
            alpha = 255
            while alpha > 0:
                
                game_screen.fill(COLOURS.WHITE)
                player_pokemon.draw_hp()
                rival_pokemon.draw_hp()
                

                if rival_pokemon.current_hp == 0:
                    player_pokemon.draw()
                    rival_pokemon.draw(alpha)
                    display_message(f'{rival_pokemon.name} Derrotado!')
                    
                else:
                    player_pokemon.draw(alpha)
                    rival_pokemon.draw()
                    display_message(f'{player_pokemon.name} Derrotado!')
                alpha -= .4
                
                pygame.display.update()
                
            game_status = 'gameover'

        if game_status == 'gameover':
            
            display_message('Play again (Y/N)?')

def drawBatlle(player_pokemon,rival_pokemon):
    game_screen.fill(COLOURS.WHITE)
    player_pokemon.draw()
    rival_pokemon.draw()
    player_pokemon.draw_hp()
    rival_pokemon.draw_hp()

def create_button(width, height, left, top, text_cx, text_cy, label):
    

    mouse_cursor = pygame.mouse.get_pos()
    
    button = Rect(left, top, width, height)

    if button.collidepoint(mouse_cursor):
        pygame.draw.rect(game_screen, COLOURS.GOLD, button)
    else:
        pygame.draw.rect(game_screen, COLOURS.WHITE, button)
        
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    text = font.render(f'{label}', True, COLOURS.BLACK)
    text_rect = text.get_rect(center=(text_cx, text_cy))
    game_screen.blit(text, text_rect)
    
    return button



