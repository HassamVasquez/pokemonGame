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
     self.bicho_btn = ActionButton(85, 120, bicho_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.dragon_btn = ActionButton(195, 120, dragon_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.electrico_btn = ActionButton(305, 120, electrico_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.agua_btn = ActionButton(415, 120, agua_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.fantasma_btn = ActionButton(525, 120, fantasma_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.fuego_btn = ActionButton(635, 120, fuego_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.hada_btn = ActionButton(745, 120, hada_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.hielo_btn = ActionButton(855, 120, hielo_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.lucha_btn = ActionButton(965, 120, lucha_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.metal_btn = ActionButton(1075, 120, metal_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.normal_btn = ActionButton(1185, 120, normal_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.planta_btn = ActionButton(85, 270, planta_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.psiquico_btm = ActionButton(195, 270, psiquico_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.roca_btn = ActionButton(305, 270, roca_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.siniestro_btn = ActionButton(415, 270, siniestro_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.tierra_btn = ActionButton(525, 270, tiera_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.veneno_btn = ActionButton(635, 270, veneno_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.volador_btn = ActionButton(745, 270, volador_img, '', hover_scale=1.08,scale=0.4,changeBgOnDisabled=False)
     self.primera_gen_btn = ActionButton(103, 450, primera_gen_img, '', hover_scale=1.08,scale=0.9,changeBgOnDisabled=False)
     self.segunda_gen_btn = ActionButton(318, 450, segunda_gen_img, '', hover_scale=1.08,scale=0.9,changeBgOnDisabled=False)
     self.tercera_gen_btn = ActionButton(533, 450, tercera_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.cuarta_gen_btn = ActionButton(748, 450, cuarta_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.quinta_gen_btn = ActionButton(963, 450, quinta_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.sexta_gen_btn = ActionButton(1178, 450, sexta_gen_img, '', hover_scale=1.08,scale=0.8,changeBgOnDisabled=False)
     self.back_button = ActionButton(420, 675, button_bg_orange, 'BACK', 1.2, 1.08)
     self.clean_btn = ActionButton(640, 675, button_bg_blue, 'CLEAN', hover_scale=1.08,scale=1.2)
     self.filter_btn = ActionButton(860, 675, button_bg_red, 'FILTER', hover_scale=1.08,scale=1.2)
     self.showing_details: list[bool] = [False]
     self.filter_list={
      "type": [],
      "gen":[],
     }
     #selected filters
     self.selec_filt = pygame.font.SysFont('consolas', 22, bold=True)
     self.msg = pygame.font.SysFont('consolas', 30, bold=True)
     
    def loop(self, screen: pygame.Surface, pokemon_list_filtered:list[Pokemon], pokemon_list:list[Pokemon], state: list[GameState], listingView: ListingView) -> None:
        types,generations=' '.join(self.filter_list['type']),' '.join(self.filter_list['gen'])
        filters = self.selec_filt.render(f'Selected Filters: ', True, COLOURS.BLACK)
        screen.blit(filters, (470, 540))
        filters = self.selec_filt.render(f'Types: {types}', True, COLOURS.BLACK)
        screen.blit(filters, (470, 565))
        filters = self.selec_filt.render(f'Generations: {generations}', True, COLOURS.BLACK)
        screen.blit(filters, (470, 590))
        mesage = self.msg.render(f'Pokemon Types: ', True, COLOURS.BLACK)
        screen.blit(mesage, (20, 20))
        mesage = self.msg.render(f'Pokemon Generations: ', True, COLOURS.BLACK)
        screen.blit(mesage, (20, 350))
        if self.bicho_btn.draw(screen, len(self.filter_list['type'])==2 or 'Bug' in self.filter_list['type']):
          self.filter_list['type'].append('Bug')

        if self.dragon_btn.draw(screen, len(self.filter_list['type'])==2 or 'Dragon' in self.filter_list['type']):
          self.filter_list['type'].append('Dragon')
          
        if self.electrico_btn.draw(screen, len(self.filter_list['type'])==2 or 'Electric' in self.filter_list['type']):
         self.filter_list['type'].append('Electric')
         
        if self.agua_btn.draw(screen, len(self.filter_list['type'])==2 or 'Water' in self.filter_list['type']):
          self.filter_list['type'].append('Water')
          
        if self.fantasma_btn.draw(screen, len(self.filter_list['type'])==2 or 'Ghost' in self.filter_list['type']):
          self.filter_list['type'].append('Ghost')
          
        if self.fuego_btn.draw(screen, len(self.filter_list['type'])==2 or 'Fire' in self.filter_list['type']):
          self.filter_list['type'].append('Fire')
          
        if self.hada_btn.draw(screen,len(self.filter_list['type'])==2 or 'Fairy' in self.filter_list['type']):
          self.filter_list['type'].append('Fairy')
       
        if self.hielo_btn.draw(screen, len(self.filter_list['type'])==2 or 'Ice' in self.filter_list['type']):
          self.filter_list['type'].append('Ice')
          
        if self.lucha_btn.draw(screen, len(self.filter_list['type'])==2 or 'Fighting' in self.filter_list['type']):
          self.filter_list['type'].append('Fighting')
          
        if self.metal_btn.draw(screen, len(self.filter_list['type'])==2 or 'Steel' in self.filter_list['type']):
         self.filter_list['type'].append('Steel')
        
        if self.normal_btn.draw(screen, len(self.filter_list['type'])==2 or 'Normal' in self.filter_list['type']):
          self.filter_list['type'].append('Normal')
          
        if self.planta_btn.draw(screen, len(self.filter_list['type'])==2 or 'Grass' in self.filter_list['type']):
          self.filter_list['type'].append('Grass')
        
        if self.psiquico_btm.draw(screen, len(self.filter_list['type'])==2 or 'Psychic' in self.filter_list['type']):
          self.filter_list['type'].append('Psychic')
          
        if self.roca_btn.draw(screen, len(self.filter_list['type'])==2 or 'Rock' in self.filter_list['type']):
          self.filter_list['type'].append('Rock')
          
        if self.siniestro_btn.draw(screen, len(self.filter_list['type'])==2 or 'Dark' in self.filter_list['type']):
         self.filter_list['type'].append('Dark')
        
        if self.tierra_btn.draw(screen, len(self.filter_list['type'])==2 or 'Ground' in self.filter_list['type']):
          self.filter_list['type'].append('Ground')
         
        if self.veneno_btn.draw(screen, len(self.filter_list['type'])==2 or 'Poison' in self.filter_list['type']):
          self.filter_list['type'].append('Poison')
         
        if self.volador_btn.draw(screen, len(self.filter_list['type'])==2 or 'Flying' in self.filter_list['type']):
          self.filter_list['type'].append('Flying')
        #generaciones
        if self.primera_gen_btn.draw(screen, len(self.filter_list['gen'])==6 or '1' in self.filter_list['gen']):
          self.filter_list['gen'].append('1')
         
        if self.segunda_gen_btn.draw(screen, len(self.filter_list['gen'])==6 or '2' in self.filter_list['gen']):
           self.filter_list['gen'].append('2')
         
        if self.tercera_gen_btn.draw(screen, len(self.filter_list['gen'])==6 or '3' in self.filter_list['gen']):
          self.filter_list['gen'].append('3')
         
        if self.cuarta_gen_btn.draw(screen, len(self.filter_list['gen'])==6 or '4' in self.filter_list['gen']):
         self.filter_list['gen'].append('4')
         
        if self.quinta_gen_btn.draw(screen,len(self.filter_list['gen'])==6 or '5' in self.filter_list['gen']):
          self.filter_list['gen'].append('5')
         
        if self.sexta_gen_btn.draw(screen, len(self.filter_list['gen'])==6 or '6' in self.filter_list['gen']):
           self.filter_list['gen'].append('6')
        
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
          
        