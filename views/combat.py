import pygame
from pygame.locals import *
import time

import random

from classes.pokemon_combat import PokemonCombat
from classes.action_button import ActionButton

import definitions.colours as COLOURS
from definitions.game_state import GameState
from definitions.team_battle import TeamBattle

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

        #Background
        ran = str(random.randint(1, 18))
        self.backGround = pygame.image.load("images/combat/backGround/"+ran+".png")
        self.backGround = pygame.transform.scale(self.backGround, (1280, 550))
        game_screen.blit(self.backGround,(0,0))

        #Backgraund bar
        self.backGroundBar = pygame.image.load("images/combat/bar.png")
        self.backGroundBar = pygame.transform.scale(self.backGroundBar, (1280, 170))
        game_screen.blit(self.backGroundBar,(0,550))
        
        #Winner
        self.winner = pygame.image.load("images/combat/winner.jpeg")
        self.winner = pygame.transform.scale(self.winner, (1280, 720))

        #HpBar
        self.bar = pygame.image.load("images/combat/bar.png")
        self.bar = pygame.transform.scale(self.bar, (400, 110))

        #Pokeball
        self.pokeball = pygame.image.load("images/combat/pokeball.png")
        self.pokeball = pygame.transform.scale(self.pokeball, (50, 50))

        game_screen.blit(self.bar,(250,75))
        game_screen.blit(self.bar,(800,400))

        #moves
        self.player_pokemon.set_moves()
        self.rival_pokemon.set_moves()

        #Buttons
        button_backgroundGreen = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()
        button_backgroundRed = pygame.image.load('images/buttons/red_button_bg.png').convert_alpha()

        button_backgroundOrange = pygame.image.load('images/buttons/orange_button_bg.png').convert_alpha()
        button_backgroundBlue = pygame.image.load('images/buttons/blue_button_bg.png').convert_alpha()
        button_backgroundYellow = pygame.image.load('images/buttons/yellow_button_bg.png').convert_alpha()
        # Button instances
        self.atack_button = ActionButton(850, 625, button_backgroundRed, 'Attack', hover_scale=1.08,scale = 1.50)
        self.potion_button = ActionButton(1150, 625, button_backgroundGreen, 'Potion', hover_scale=1.08, scale = 1.50)

        #Buttons movens
        self.mov1_button = ActionButton(850, 595, button_backgroundOrange, self.player_pokemon.moves[0]['name'], hover_scale=1.08,scale = 1.2, fontTam = 22)
        self.mov2_button = ActionButton(850, 680, button_backgroundBlue, self.player_pokemon.moves[1]['name'], hover_scale=1.08, scale = 1.2, fontTam = 22)
        self.mov3_button = ActionButton(1150, 595, button_backgroundBlue, self.player_pokemon.moves[2]['name'], hover_scale=1.08, scale = 1.2, fontTam = 22)
        self.mov4_button = ActionButton(1150, 680, button_backgroundOrange, self.player_pokemon.moves[3]['name'], hover_scale=1.08, scale = 1.2, fontTam = 22)
        
        #Buttons back, play again
        self.playAgain = ActionButton(900, 200, button_backgroundYellow, "Play again", hover_scale=1.08,scale = 1.2, fontTam = 22)
        self.exit = ActionButton(900, 400, button_backgroundYellow, "Exit", hover_scale=1.08, scale = 1.2, fontTam = 22 )

        #Button next battle
        self.nextBattle = ActionButton(900, 300, button_backgroundYellow, "Next battle", hover_scale=1.08,scale = 1.2, fontTam = 22)

    def loop(self, game_screen: pygame.Surface, state: list[GameState], flagTeam: list[TeamBattle], numPokemon = 1) -> None:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state[0] = GameState.LISTING
        
        if self.game_status == 'BattlePokemon':
            
            game_screen.blit(self.backGround,(0,0))
            game_screen.blit(self.backGroundBar,(0,550))

            self.bandera = 0
            self.player_pokemon.current_hp = 130
            self.rival_pokemon.current_hp = 130
            
            self.player_pokemon.x = 200
            self.player_pokemon.y = 300
            self.rival_pokemon.x = 850
            self.rival_pokemon.y = 100

            self.rival_pokemon.draw(game_screen,scale=220)
            display_message(game_screen, f'The rival choose  {self.rival_pokemon.name}!')
            time.sleep(2)
            
            game_screen.blit(self.backGroundBar,(0,550))

            self.rival_pokemon.draw(game_screen,scale=220)
            self.player_pokemon.draw(game_screen)
            display_message(game_screen , f'Go {self.player_pokemon.name}!')
            time.sleep(2)

            self.player_pokemon.hp_x = 1000
            self.player_pokemon.hp_y = 440
            self.rival_pokemon.hp_x = 450
            self.rival_pokemon.hp_y = 115

            self.dataBox(game_screen, numPokemon)
            self.game_status = 'player turn'

        if self.game_status == 'player turn':
            game_screen.blit(self.backGround,(0,0))
            game_screen.blit(self.backGroundBar,(0,550))

            self.dataBox(game_screen, numPokemon)

            drawBatlle(self.player_pokemon,self.rival_pokemon,game_screen)
            
            if self.bandera == 0:
                self.display_message_box(game_screen, "Choose your action",100, 625 )
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
                if self.rival_pokemon.current_hp == 0:
                    self.game_status = 'fainted'
                else:
                    self.game_status = 'rival turn'
            
            if self.bandera == 3:
                game_screen.blit(self.backGroundBar,(0,550))
                if self.player_pokemon.num_potions == 0:
                        display_message(game_screen ,'No more potions left')
                        time.sleep(2)
                        self.bandera = 1
                else:
                    self.player_pokemon.use_potion()
                    display_message(game_screen ,f'{self.player_pokemon.name} used potion')
                    time.sleep(2)
                    self.game_status = 'rival turn'
                    self.bandera = 2
            #pygame.draw.rect(game_screen, COLOURS.BLACK, (10, 350, 480, 140), 3)

        if self.game_status == 'rival turn':
            game_screen.blit(self.backGround,(0,0))
            game_screen.blit(self.backGroundBar,(0,550))
            self.dataBox(game_screen, numPokemon)

            drawBatlle(self.player_pokemon,self.rival_pokemon,game_screen)
            
            move = random.choice(self.rival_pokemon.moves)
            self.rival_pokemon.perform_attack(self.player_pokemon, move, self.rival_pokemon,0)
            if self.player_pokemon.current_hp == 0:
                self.game_status = 'fainted'
            else:
                self.game_status = 'player turn'
                self.bandera = 0
            

        if self.game_status == 'fainted':
            game_screen.blit(self.backGround,(0,0))
            game_screen.blit(self.backGroundBar,(0,550))
            self.dataBox(game_screen, numPokemon)
            alpha = 75
            while alpha > 0:

                if self.rival_pokemon.current_hp == 0:
                    self.player_pokemon.draw(game_screen)
                    self.rival_pokemon.draw(game_screen,alpha,scale=220)
                    display_message(game_screen , f'{self.rival_pokemon.name} Derrotado!')
                    self.winnerPokemon = self.player_pokemon

                else:
                    self.player_pokemon.draw(game_screen,alpha)
                    self.rival_pokemon.draw(game_screen,scale=220)
                    display_message(game_screen ,f'{self.player_pokemon.name} Derrotado!')
                    self.winnerPokemon = self.rival_pokemon
                alpha -= .4
            if numPokemon > 1 :
                self.game_status = 'gameoverTeam'

            else: 
                self.game_status = 'gameover'

        if self.game_status == 'gameover':
            game_screen.blit(self.winner,(0,0))
            self.winnerPokemon.x = 250
            self.winnerPokemon.y = 150
            self.winnerPokemon.draw(game_screen)
            if self.playAgain.draw(game_screen):
                self.game_status = 'BattlePokemon'
               
            if self.exit.draw(game_screen):
                state[0] = GameState.LISTING
                self.game_status = 'BattlePokemon'
        
        if self.game_status == 'gameoverTeam':
            game_screen.blit(self.winner,(0,0))
            self.winnerPokemon.x = 250
            self.winnerPokemon.y = 150
            self.winnerPokemon.draw(game_screen)
            if self.nextBattle.draw(game_screen):
                flagTeam[0] = TeamBattle.DEFINITIONS
                #

        pygame.display.update()

    def dataBox(self,game_screen: pygame.Surface, numPokemon = 1 ,):
        game_screen.blit(self.bar,(250,75))
        game_screen.blit(self.bar,(800,400))
        x = 1050
        for i in range(numPokemon):
            game_screen.blit(self.pokeball,(x,355))
            x = x + 50
        x = 500
        for i in range(numPokemon):
            game_screen.blit(self.pokeball,(x,30))
            x = x + 50

        self.display_message_box(game_screen ,f'{self.player_pokemon.name}', 830,  420)
        self.display_message_box(game_screen ,f'{self.rival_pokemon.name}', 280,  95)
        self.player_pokemon.draw_hp(game_screen)
        self.rival_pokemon.draw_hp(game_screen)

    def display_message_box(self,game_screen: pygame.Surface, message,x , y ):
        font = pygame.font.Font(pygame.font.get_default_font(), 25)
        text = font.render(message, True, COLOURS.BLACK)
        text_rect = text.get_rect()
        text_rect.x = x
        text_rect.y = y
        game_screen.blit(text, text_rect)