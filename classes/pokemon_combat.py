import pygame
import random
import math
import time

from definitions import colours as COLOURS

from utils.display import display_message
from utils.display import drawBatlle

#Movimientos

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


#Clase de pokemons que van a pelear
class PokemonCombat(pygame.sprite.Sprite):

    def __init__(self, name, level, x, y, route,type,gameScreen: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.name,self.level,self.x,self.y,self.route,self.max_hp, self.current_hp= name,level,x,y,route,100 + level, 130
        self.type = type
        self.size = 150
        self.num_potions = 3
        self.gameScreen= gameScreen
        self.hp_x = 0
        self.hp_y = 0
        self.set_sprite()
    
    def set_sprite(self):
        self.image = pygame.image.load(self.route)
        scale = self.size/self.image.get_width()
        new_width,new_height = self.image.get_width() * scale,self.image.get_height()* scale
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
    
    def draw(self,game_screen : pygame.Surface,alpha = 255):
        sprite, transparency= self.image.copy(),(255,255,255,alpha)
        sprite.fill(transparency,None,pygame.BLEND_RGB_MULT)
        game_screen.blit(sprite,(self.x,self.y))
    
    def draw_hp(self,game_screen : pygame.Surface):
        
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
            drawBatlle(me,rival,self.gameScreen)
        elif band ==0 :
            drawBatlle(rival,me,self.gameScreen)
        name = move['name']
        display_message(self.gameScreen,f'{self.name} used {name}')
        
        damage = move['atack']

        damage = math.floor(damage)

        rival.take_damage(damage)
        
    def take_damage(self, damage):
        print("Entre a take Damage")
        self.current_hp -= damage
        
        if self.current_hp < 0:
            self.current_hp = 0
        time.sleep(1)
    def use_potion(self):
        if self.num_potions > 0:
            
            self.current_hp += 30
            if self.current_hp > self.max_hp:
                self.current_hp = self.max_hp
                
            self.num_potions -= 1