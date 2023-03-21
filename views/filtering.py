import pygame
from classes.action_button import ActionButton
from classes.pokemon import Pokemon
from views.listing import ListingView
from utils.function_filters import list_filtred
from definitions.game_state import GameState

class FilteringView():
    def __init__(self,) -> None:
     quit_img = pygame.image.load("images/filtros/button_quit.png").convert_alpha()
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
     filter_img = pygame.image.load('images/filtros/filtro.png').convert_alpha()
     back_img = pygame.image.load('images/filtros/button_back.png').convert_alpha()

        #create button instances
     self.filtros_btn = ActionButton(300, 680, filter_img, '', hover_scale=1.08)
     self.quit_button = ActionButton(300, 680, quit_img, '', hover_scale=1.08)
     self.bicho_btn = ActionButton(85, 100, bicho_img, '', hover_scale=1.08,scale=0.4)
     self.dragon_btn = ActionButton(195, 100, dragon_img, '', hover_scale=1.08,scale=0.4)
     self.electrico_btn = ActionButton(305, 100, electrico_img, '', hover_scale=1.08,scale=0.4)
     self.agua_btn = ActionButton(415, 100, agua_img, '', hover_scale=1.08,scale=0.4)
     self.fantasma_btn = ActionButton(525, 100, fantasma_img, '', hover_scale=1.08,scale=0.4)
     self.fuego_btn = ActionButton(635, 100, fuego_img, '', hover_scale=1.08,scale=0.4)
     self.hada_btn = ActionButton(745, 100, hada_img, '', hover_scale=1.08,scale=0.4)
     self.hielo_btn = ActionButton(855, 100, hielo_img, '', hover_scale=1.08,scale=0.4)
     self.lucha_btn = ActionButton(965, 100, lucha_img, '', hover_scale=1.08,scale=0.4)
     self.metal_btn = ActionButton(1075, 100, metal_img, '', hover_scale=1.08,scale=0.4)
     self.normal_btn = ActionButton(1185, 100, normal_img, '', hover_scale=1.08,scale=0.4)
     self.planta_btn = ActionButton(85, 250, planta_img, '', hover_scale=1.08,scale=0.4)
     self.psiquico_btm = ActionButton(195, 250, psiquico_img, '', hover_scale=1.08,scale=0.4)
     self.roca_btn = ActionButton(305, 250, roca_img, '', hover_scale=1.08,scale=0.4)
     self.siniestro_btn = ActionButton(415, 250, siniestro_img, '', hover_scale=1.08,scale=0.4)
     self.tierra_btn = ActionButton(525, 250, tiera_img, '', hover_scale=1.08,scale=0.4)
     self.veneno_btn = ActionButton(635, 250, veneno_img, '', hover_scale=1.08,scale=0.4)
     self.volador_btn = ActionButton(745, 250, volador_img, '', hover_scale=1.08,scale=0.4)
     self.primera_gen_btn = ActionButton(103, 400, primera_gen_img, '', hover_scale=1.08,scale=0.9)
     self.segunda_gen_btn = ActionButton(318, 400, segunda_gen_img, '', hover_scale=1.08,scale=0.9)
     self.tercera_gen_btn = ActionButton(533, 400, tercera_gen_img, '', hover_scale=1.08,scale=0.8)
     self.cuarta_gen_btn = ActionButton(748, 400, cuarta_gen_img, '', hover_scale=1.08,scale=0.8)
     self.quinta_gen_btn = ActionButton(963, 400, quinta_gen_img, '', hover_scale=1.08,scale=0.8)
     self.sexta_gen_btn = ActionButton(1178, 400, sexta_gen_img, '', hover_scale=1.08,scale=0.8)
     self.filter_btn = ActionButton(1178, 610, filter_img, '', hover_scale=1.08,scale=0.6)
     self.back_button = ActionButton(100, 620, back_img, '', hover_scale=1.08,scale=0.7)
     self.filter_list={
      "type": [],
      "gen":[],
     }

    def loop(self, screen: pygame.Surface, pokemon_list_filtered:list[Pokemon], pokemon_list:list[Pokemon], state: list[GameState], listingView: ListingView) -> None:
        if self.bicho_btn.draw(screen):
          if 'Bug' not in self.filter_list['type']:
            self.filter_list['type'].append('Bug')
          
        if self.dragon_btn.draw(screen):
          if 'Dragon' not in self.filter_list['type']:
            self.filter_list['type'].append('Dragon')
          
        if self.electrico_btn.draw(screen):
          type_data='Electric'
          if 'Electric' not in self.filter_list['type']:
            self.filter_list['type'].append('Electric')
         
        if self.agua_btn.draw(screen):
          type_data='Water'
          if 'Water' not in self.filter_list['type']:
            self.filter_list['type'].append('Water')
          
        if self.fantasma_btn.draw(screen):
          type_data='Ghost'
          if 'Ghost' not in self.filter_list['type']:
            self.filter_list['type'].append('Ghost')
          
        if self.fuego_btn.draw(screen):
          if 'Fire' not in self.filter_list['type']:
            self.filter_list['type'].append('Fire')
          
        if self.hada_btn.draw(screen):
          if 'Fairy' not in self.filter_list['type']:
            self.filter_list['type'].append('Fairy')
       
        if self.hielo_btn.draw(screen):
          type_data='Ice'
          if 'Ice' not in self.filter_list['type']:
            self.filter_list['type'].append('Ice')
          
        if self.lucha_btn.draw(screen):
          type_data='Fighting'
          if 'Fighting' not in self.filter_list['type']:
            self.filter_list['type'].append('Fighting')
          
        if self.metal_btn.draw(screen):
         if 'Steel' not in self.filter_list['type']:
            self.filter_list['type'].append('Steel')
        
        if self.normal_btn.draw(screen):
          if 'Normal' not in self.filter_list['type']:
            self.filter_list['type'].append('Normal')
          
        if self.planta_btn.draw(screen):
          if 'Grass' not in self.filter_list['type']:
            self.filter_list['type'].append('Grass')
        
        if self.psiquico_btm.draw(screen):
          if 'Psychic' not in self.filter_list['type']:
            self.filter_list['type'].append('Psychic')
          
        if self.roca_btn.draw(screen):
          type_data='Rock'
          if 'Rock' not in self.filter_list['type']:
            self.filter_list['type'].append('Rock')
          
        if self.siniestro_btn.draw(screen):
         if 'Dark' not in self.filter_list['type']:
            self.filter_list['type'].append('Dark')
        
        if self.tierra_btn.draw(screen):
          if 'Ground' not in self.filter_list['type']:
            self.filter_list['type'].append('Ground')
         
        if self.veneno_btn.draw(screen):
          if 'Poison' not in self.filter_list['type']:
            self.filter_list['type'].append('Poison')
         
        if self.volador_btn.draw(screen):
          if 'Flying' not in self.filter_list['type']:
            self.filter_list['type'].append('Flying')
        #generaciones
        if self.primera_gen_btn.draw(screen):
          type_data='1'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.segunda_gen_btn.draw(screen):
          type_data='2'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.tercera_gen_btn.draw(screen):
          type_data='3'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.cuarta_gen_btn.draw(screen):
          type_data='4'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.quinta_gen_btn.draw(screen):
          type_data='5'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
         
        if self.sexta_gen_btn.draw(screen):
          type_data='6'
          if type_data not in self.filter_list['gen']:
            self.filter_list['gen'].append(type_data)
        
        if self.filter_btn.draw(screen):
          pokemon_list_filtered.clear()
          pokemon_list_filtered.extend(list_filtred(pokemon_list,self.filter_list))
          state[0] = GameState.LISTING
          listingView.update(pokemon_list_filtered)
        if self.back_button.draw(screen):
          state[0] = GameState.LISTING
          
        