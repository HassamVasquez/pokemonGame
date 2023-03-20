import pygame
from pygame.locals import *
import time

import random

from classes.pokemon_combat import PokemonCombat
from classes.action_button import ActionButton

import definitions.colours as COLOURS
from definitions.game_state import GameState

from utils.display import changeTamDisplay
from utils.display import create_button
from utils.display import display_message
from utils.display import drawBatlle


class Combat():
    def __init__(self, pokemon_list: list[PokemonCombat],game_screen: pygame.Surface) -> None:
        self.rival_pokemon = pokemon_list[1]
        self.player_pokemon = pokemon_list[0]
        self.game_status = 'BattlePokemon'
        self.fight_button = 0
        self.potion_button = 0
        self.move_buttons = []
        self.move = 0
        self.bandera = 0

        #Inicializamos movimientos
        self.player_pokemon.set_moves()
        self.rival_pokemon.set_moves()

        button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()

        # Button instances
        self.atack_button = ActionButton(125, 420, button_background, 'Atack', hover_scale=1.08,scale = 1.50)
        self.potion_button = ActionButton(372, 420, button_background, 'Potion', hover_scale=1.08, scale = 1.50)

        #Botones de movimientos
        self.mov1_button = ActionButton(100, 375, button_background, self.player_pokemon.moves[0]['name'], hover_scale=1.08,scale = 1.2, fontTam = 22)
        self.mov2_button = ActionButton(350, 375, button_background, self.player_pokemon.moves[1]['name'], hover_scale=1.08, scale = 1.2, fontTam = 22)
        self.mov3_button = ActionButton(100, 450, button_background, self.player_pokemon.moves[2]['name'], hover_scale=1.08, scale = 1.2, fontTam = 22)
        self.mov4_button = ActionButton(350, 450, button_background, self.player_pokemon.moves[3]['name'], hover_scale=1.08, scale = 1.2, fontTam = 22)
        
        #Cambiamos display
        

    def loop(self, game_screen: pygame.Surface, pokemon_list, state: list[GameState]) -> None:
        changeTamDisplay(500,500)
        for event in pygame.event.get():

            game_screen.fill(COLOURS.WHITE)
            if event.type == KEYDOWN:

                if event.key == K_y:
                    self.player_pokemon.current_hp = 130
                    self.rival_pokemon.current_hp = 130
                    self.player_pokemon.num_potions = 3
                    self.game_status = 'BattlePokemon'
                elif event.key == K_n:
                    #Change display
                    changeTamDisplay(1280, 720)
                    state[0] = GameState.LISTING
                    

            
        if self.game_status == 'BattlePokemon':
            
            self.player_pokemon.x = 0
            self.player_pokemon.y = 175
            self.rival_pokemon.x = 300
            self.rival_pokemon.y = -10
            alpha = 0
            while alpha < 100:
                game_screen.fill(COLOURS.WHITE)
                self.rival_pokemon.draw(game_screen,alpha)
                display_message(game_screen, f'El rival eligio a  {self.rival_pokemon.name}!')
                alpha += .4
                
                pygame.display.update()
            alpha = 0
            while alpha < 100:
                game_screen.fill(COLOURS.WHITE)
                self.rival_pokemon.draw(game_screen)
                self.player_pokemon.draw(game_screen,alpha)
                display_message(game_screen , f'Ve {self.player_pokemon.name}!')
                alpha += .4
                
                pygame.display.update()
            self.player_pokemon.hp_x = 275
            self.player_pokemon.hp_y = 250
            self.rival_pokemon.hp_x = 50
            self.rival_pokemon.hp_y = 50

            self.player_pokemon.draw_hp(game_screen)
            self.rival_pokemon.draw_hp(game_screen)
            
            self.game_status = 'player turn'
            self.bandera == 0

        if self.game_status == 'player turn':
            game_screen.fill(COLOURS.WHITE)
            drawBatlle(self.player_pokemon,self.rival_pokemon,game_screen)
            if self.bandera == 0:
                if self.atack_button.draw(game_screen):
                    self.bandera = 1
                if self.potion_button.draw(game_screen):
                    self.bandera = 3

            if self.bandera == 1:
                if self.mov1_button.draw(game_screen):
                    self.player_pokemon.perform_attack(self.rival_pokemon, self.player_pokemon.moves[0],self.player_pokemon,1)
                    self.bandera = 2
                if self.mov2_button.draw(game_screen):
                    self.player_pokemon.perform_attack(self.rival_pokemon, self.player_pokemon.moves[1],self.player_pokemon,1)
                    self.bandera = 2
                if self.mov3_button.draw(game_screen):
                    self.player_pokemon.perform_attack(self.rival_pokemon, self.player_pokemon.moves[2],self.player_pokemon,1)
                    self.bandera = 2
                if self.mov4_button.draw(game_screen):
                    self.player_pokemon.perform_attack(self.rival_pokemon, self.player_pokemon.moves[3],self.player_pokemon,1)
                    self.bandera = 2

            if self.bandera == 2:
                game_screen.fill(COLOURS.WHITE)
                if self.rival_pokemon.current_hp == 0:
                    
                    self.game_status = 'fainted'
                else:
                    self.game_status = 'rival turn'
            
            if self.bandera == 3:
                if self.player_pokemon.num_potions == 0:
                        display_message(game_screen ,'No more potions left')
                        time.sleep(1)
                        self.bandera = 1
                else:
                    self.player_pokemon.use_potion()
                    display_message(game_screen ,f'{self.player_pokemon.name} used potion')
                    time.sleep(1)
                    self.game_status = 'rival turn'
                    self.bandera = 2
            #pygame.draw.rect(game_screen, COLOURS.BLACK, (10, 350, 480, 140), 3)

        if self.game_status == 'rival turn':
            game_screen.fill(COLOURS.WHITE)
            drawBatlle(self.player_pokemon,self.rival_pokemon,game_screen)
            
            
            move = random.choice(self.rival_pokemon.moves)
            self.rival_pokemon.perform_attack(self.player_pokemon, move, self.rival_pokemon,0)
            if self.player_pokemon.current_hp == 0:
                self.game_status = 'fainted'
            else:
                self.game_status = 'player turn'
                self.bandera = 0
            

        if self.game_status == 'fainted':
            
            alpha = 75
            while alpha > 0:
                
                game_screen.fill(COLOURS.WHITE)
                self.player_pokemon.draw_hp(game_screen)
                self.rival_pokemon.draw_hp(game_screen)
                

                if self.rival_pokemon.current_hp == 0:
                    self.player_pokemon.draw(game_screen)
                    self.rival_pokemon.draw(game_screen,alpha)
                    display_message(game_screen , f'{self.rival_pokemon.name} Derrotado!')
                    
                else:
                    self.player_pokemon.draw(game_screen,alpha)
                    self.rival_pokemon.draw(game_screen)
                    display_message(game_screen ,f'{self.player_pokemon.name} Derrotado!')
                alpha -= .4
                
                
                
            self.game_status = 'gameover'

        if self.game_status == 'gameover':
            
            display_message(game_screen ,'Play again (Y/N)?')
        pygame.display.update()