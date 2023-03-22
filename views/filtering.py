import pygame
from classes.action_button import ActionButton
from classes.pokemon import Pokemon
from views.listing import ListingView
from utils.function_filters import list_filtred
from definitions.game_state import GameState
import definitions.colours as COLOURS

class FilteringView():
    def __init__(self,) -> None:
     bicho_img = pygame.image.load('images/filtros/bicho.png').convert_alpha()
     dragon_img = pygame.image.load('images/filtros/dragon.png').convert_alpha()
     electrico_img = pygame.image.load('images/filtros/electrico.png').convert_alpha()
     agua_img = pygame.image.load('images/filtros/agua.png').convert_alpha()
     fantasma_img = pygame.image.load('images/filtros/fantasma.png').convert_alpha()#
     fuego_img = pygame.image.load('images/filtros/fuego.png').convert_alpha()
     hada_img = pygame.image.load('images/filtros/hada.png').convert_alpha()
     hielo_img = pygame.image.load('images/filtros/hielo.png').convert_alpha()
     lucha_img = pygame.image.load('images/filtros/lucha.png').convert_alpha()
     metal_img = pygame.image.load('images/filtros/metal.png').convert_alpha()
     normal_img = pygame.image.load('images/filtros/normal.png').convert_alpha()
     planta_img = pygame.image.load('images/filtros/planta.png').convert_alpha()
     psiquico_img = pygame.image.load('images/filtros/psiquico.png').convert_alpha()
     roca_img = pygame.image.load('images/filtros/roca.png').convert_alpha()
     siniestro_img = pygame.image.load('images/filtros/siniestro.png').convert_alpha()
     tiera_img = pygame.image.load('images/filtros/tierra.png').convert_alpha()
     veneno_img = pygame.image.load('images/filtros/veneno.png').convert_alpha()
     volador_img = pygame.image.load('images/filtros/volador.png').convert_alpha()
     primera_gen_img = pygame.image.load('images/filtros/primera.png').convert_alpha()
     segunda_gen_img = pygame.image.load('images/filtros/segunda.png').convert_alpha()
     tercera_gen_img = pygame.image.load('images/filtros/tercera.png').convert_alpha()
     cuarta_gen_img = pygame.image.load('images/filtros/cuarta.png').convert_alpha()
     quinta_gen_img = pygame.image.load('images/filtros/quinta.png').convert_alpha()
     sexta_gen_img = pygame.image.load('images/filtros/sexta.png').convert_alpha()
     button_bg_orange = pygame.image.load('images/buttons/orange_button_bg.png').convert_alpha()
     button_bg_blue = pygame.image.load('images/buttons/blue_button_bg.png').convert_alpha()
     button_bg_red = pygame.image.load('images/buttons/red_button_bg.png').convert_alpha()
        #create button instances
     self.bicho_btn = ActionButton(85, 100, bicho_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.dragon_btn = ActionButton(195, 100, dragon_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.electrico_btn = ActionButton(305, 100, electrico_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.agua_btn = ActionButton(415, 100, agua_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.fantasma_btn = ActionButton(525, 100, fantasma_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.fuego_btn = ActionButton(635, 100, fuego_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.hada_btn = ActionButton(745, 100, hada_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.hielo_btn = ActionButton(855, 100, hielo_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.lucha_btn = ActionButton(965, 100, lucha_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.metal_btn = ActionButton(1075, 100, metal_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.normal_btn = ActionButton(1185, 100, normal_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.planta_btn = ActionButton(85, 250, planta_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.psiquico_btm = ActionButton(195, 250, psiquico_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.roca_btn = ActionButton(305, 250, roca_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.siniestro_btn = ActionButton(415, 250, siniestro_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.tierra_btn = ActionButton(525, 250, tiera_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.veneno_btn = ActionButton(635, 250, veneno_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.volador_btn = ActionButton(745, 250, volador_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.primera_gen_btn = ActionButton(103, 400, primera_gen_img, '', hover_scale=1.08,scale=0.9,changeBgOnDisabled=False)
     self.segunda_gen_btn = ActionButton(318, 400, segunda_gen_img, '', hover_scale=1.08,scale=0.9,changeBgOnDisabled=False)
     self.tercera_gen_btn = ActionButton(533, 400, tercera_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.cuarta_gen_btn = ActionButton(748, 400, cuarta_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.quinta_gen_btn = ActionButton(963, 400, quinta_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.sexta_gen_btn = ActionButton(1178, 400, sexta_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.back_button = ActionButton(420, 610, button_bg_orange, 'BACK', 1.2, 1.08)
     self.clean_btn = ActionButton(640, 610, button_bg_blue, 'CLEAN', hover_scale=1.08,scale=1.2)
     self.filter_btn = ActionButton(860, 610, button_bg_red, 'FILTER', hover_scale=1.08,scale=1.2)
     self.showing_details: list[bool] = [False]
     self.filter_list={
      "type": [],
      "gen":[],
     }
     #selected filters
     self.selec_filt = pygame.font.SysFont('consolas', 22, bold=True)
     
    def loop(self, screen: pygame.Surface, pokemon_list_filtered:list[Pokemon], pokemon_list:list[Pokemon], state: list[GameState], listingView: ListingView) -> None:
        types,generations=self.filter_list['type'],self.filter_list['gen']
        filters = self.selec_filt.render(f'Selected Filters: Types: {types}, Generations: {generations}', True, COLOURS.BLACK)
        screen.blit(filters, (100, 510))
        
        if self.bicho_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Bug' not in self.filter_list['type']:
            self.filter_list['type'].append('Bug')
            
        if self.dragon_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Dragon' not in self.filter_list['type']:
            self.filter_list['type'].append('Dragon')
          
        if self.electrico_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Electric' not in self.filter_list['type']:
            self.filter_list['type'].append('Electric')
         
        if self.agua_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Water' not in self.filter_list['type']:
            self.filter_list['type'].append('Water')
          
        if self.fantasma_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Ghost' not in self.filter_list['type']:
            self.filter_list['type'].append('Ghost')
          
        if self.fuego_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Fire' not in self.filter_list['type']:
            self.filter_list['type'].append('Fire')
          
        if self.hada_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Fairy' not in self.filter_list['type']:
            self.filter_list['type'].append('Fairy')
       
        if self.hielo_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Ice' not in self.filter_list['type']:
            self.filter_list['type'].append('Ice')
          
        if self.lucha_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Fighting' not in self.filter_list['type']:
            self.filter_list['type'].append('Fighting')
          
        if self.metal_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
         if 'Steel' not in self.filter_list['type']:
            self.filter_list['type'].append('Steel')
        
        if self.normal_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Normal' not in self.filter_list['type']:
            self.filter_list['type'].append('Normal')
          
        if self.planta_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Grass' not in self.filter_list['type']:
            self.filter_list['type'].append('Grass')
        
        if self.psiquico_btm.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Psychic' not in self.filter_list['type']:
            self.filter_list['type'].append('Psychic')
          
        if self.roca_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Rock' not in self.filter_list['type']:
            self.filter_list['type'].append('Rock')
          
        if self.siniestro_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
         if 'Dark' not in self.filter_list['type']:
            self.filter_list['type'].append('Dark')
        
        if self.tierra_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Ground' not in self.filter_list['type']:
            self.filter_list['type'].append('Ground')
         
        if self.veneno_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Poison' not in self.filter_list['type']:
            self.filter_list['type'].append('Poison')
         
        if self.volador_btn.draw(screen, len(self.filter_list['type'])  not in [0, 1]):
          if 'Flying' not in self.filter_list['type']:
            self.filter_list['type'].append('Flying')
        #generaciones
        if self.primera_gen_btn.draw(screen, len(self.filter_list['gen'])  not in [0,1,2,3,4,5]):
          type_data='1'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.segunda_gen_btn.draw(screen, len(self.filter_list['gen'])  not in [0,1,2,3,4,5]):
          type_data='2'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.tercera_gen_btn.draw(screen, len(self.filter_list['gen'])  not in [0,1,2,3,4,5]):
          type_data='3'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.cuarta_gen_btn.draw(screen, len(self.filter_list['gen'])  not in [0,1,2,3,4,5]):
          type_data='4'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.quinta_gen_btn.draw(screen, len(self.filter_list['gen'])  not in [0,1,2,3,4,5]):
          type_data='5'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.sexta_gen_btn.draw(screen, len(self.filter_list['gen'])  not in [0,1,2,3,4,5]):
          type_data='6'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
        if self.clean_btn.draw(screen):
          self.filter_list={
          "type": [],
          "gen":[],
          }
          print(self.filter_list)

        if self.filter_btn.draw(screen):
          pokemon_list_filtered.clear()
          pokemon_list_filtered.extend(list_filtred(pokemon_list,self.filter_list))
          state[0] = GameState.LISTING
          listingView.update(pokemon_list_filtered)
        
        if self.back_button.draw(screen):
          state[0] = GameState.LISTING
          
        