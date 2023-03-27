import pygame
import random
import math
import time

from definitions import colours as COLOURS

from utils.display import display_message
from utils.display import drawBatlle

#Movimientos

mov_plant = [{'name': 'Frenzy Plant', 'atack': 45},{'name': 'Vine Whip', 'atack': 20},{'name': 'Leaf Blade', 'atack': 30},{'name': 'Seed Bomb', 'atack': 10}]
mov_fuego = [{'name': 'Overheat', 'atack': 30},{'name': 'Blast Burn', 'atack': 45},{'name': 'Flame Charge', 'atack': 40},{'name': 'Fire Punch', 'atack': 10}]
mov_tierra = [{'name': 'Earthquake', 'atack': 45},{'name': 'Earth Power', 'atack': 40},{'name': 'Mud Bomb', 'atack': 30},{'name': 'Mud Shot', 'atack': 10}]
mov_roca = [{'name': 'Rock Slide', 'atack': 45},{'name': 'Ancient Power', 'atack': 40},{'name': 'Power Gem', 'atack': 30},{'name': 'Rock Blast', 'atack': 10}]
mov_siniestro = [{'name': 'Crunch', 'atack': 45},{'name': 'Bite', 'atack': 40},{'name': 'Foul Play', 'atack': 30},{'name': 'Snarl', 'atack': 10}]
mov_fantasma = [{'name': 'Shadow Ball', 'atack': 100},{'name': 'Shadow Punch', 'atack': 40},{'name': 'Shadow Bone', 'atack': 30},{'name': 'Shadow Claw', 'atack': 10}]
mov_lucha = [{'name': 'Focus Blast', 'atack': 120},{'name': 'Dynamic Punch', 'atack': 40},{'name': 'Power-Up Punch', 'atack': 15},{'name': 'Counter', 'atack': 5}]
mov_electrico = [{'name': 'Wild Charge', 'atack': 45},{'name': 'Thunder Shock', 'atack': 40},{'name': 'Thunder Punch', 'atack': 30},{'name': 'Discharge', 'atack': 10}]
mov_hada= [{'name': 'Play Rough', 'atack': 45},{'name': 'Dazzling Gleam', 'atack': 40},{'name': 'Charm', 'atack': 30},{'name': 'Moonblast', 'atack': 10}]
mov_psiquico = [{'name': 'Psystrike', 'atack': 45},{'name': 'Synchronoise', 'atack': 40},{'name': 'Confusion', 'atack': 30},{'name': 'Psychic', 'atack': 10}]
mov_veneno = [{'name': 'Cross Poison', 'atack': 45},{'name': 'Gunk Shot', 'atack': 40},{'name': 'Acid Spray', 'atack': 30},{'name': 'Bug Bite', 'atack': 10}]
mov_acero = [{'name': 'Meteor Mash', 'atack': 45},{'name': 'Smart Strike', 'atack': 40},{'name': 'Flash Cannon', 'atack': 30},{'name': 'Mirror Shot', 'atack': 10}]
mov_normal = [{'name': 'Hyper Beam', 'atack': 45},{'name': 'Body Slam', 'atack': 40},{'name': 'Pound', 'atack': 30},{'name': 'Last Resort', 'atack': 10}]
mov_volador = [{'name': 'Sky Attack', 'atack': 45},{'name': 'Brave Bird', 'atack': 40},{'name': 'Hurricane', 'atack': 30},{'name': 'Dragon Ascent', 'atack': 10}]
mov_bicho = [{'name': 'Bug Bite', 'atack': 45},{'name': 'Lunge', 'atack': 40},{'name': 'Bug Buzz', 'atack': 30},{'name': 'Infestation', 'atack': 10}]
mov_agua = [{'name': 'Hydro Pump', 'atack': 45},{'name': 'Water Pulse', 'atack': 40},{'name': 'Aqua Tail', 'atack': 30},{'name': 'Water Gun', 'atack': 10}]
mov_hielo = [{'name': 'Weather Ball', 'atack': 45},{'name': 'Blizzard', 'atack': 40},{'name': 'Ice Beam', 'atack': 30},{'name': 'Ice Punch', 'atack': 10}]
mov_dragon = [{'name': 'Outrage', 'atack': 100},{'name': 'Draco Meteor', 'atack': 40},{'name': 'Dragon Claw', 'atack': 30},{'name': 'Dragon Tail', 'atack': 10}]


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
        self.message = ""
        self.set_sprite()


    def set_sprite(self):
        self.image = pygame.image.load(self.route)
        scale = self.size/self.image.get_width()
        new_width,new_height = self.image.get_width() * scale,self.image.get_height()* scale
        self.image = pygame.transform.scale(self.image,(new_width,new_height))
    
    def draw(self,game_screen : pygame.Surface,alpha = 255,scale = 250):
        sprite, transparency= self.image.copy(),(255,255,255,alpha)
        sprite = pygame.transform.scale(sprite, (scale, scale))
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
        if self.name == 'Magikarp': self.moves = [{'name': 'Water Spout ', 'atack': 1}]
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
        time.sleep(2)
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