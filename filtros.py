import pygame,sys,listado
from pygame.locals import *
import button

pygame.init()
#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")
#define fonts
font = pygame.font.SysFont("arialblack", 50)
#define colours
TEXT_COL = (255, 255, 255)
filter_list = []
def add_filter(filter):
  filter_list.append(filter)
def make_filter():
  print(filter_list)
#load button images
resume_img = pygame.image.load("images/filtros/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/filtros/button_options.png").convert_alpha()
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
filtros_btn = button.Button(400, 600, filter_img, 0.5)
quit_button = button.Button(336, 375, quit_img, 1)
bicho_btn = button.Button(20, 10, bicho_img, 0.4)
dragon_btn = button.Button(150, 9, dragon_img, 0.4)
electrico_btn = button.Button(300, 10, electrico_img, 0.4)
agua_btn = button.Button(440, 10, agua_img, 0.4)
fantasma_btn = button.Button(570, 10, fantasma_img, 0.4)
fuego_btn = button.Button(710, 10, fuego_img, 0.4)
hada_btn = button.Button(850, 10, hada_img, 0.4)
hielo_btn = button.Button(20, 145, hielo_img, 0.4)
lucha_btn = button.Button(150, 145, lucha_img, 0.4)
metal_btn = button.Button(300, 145, metal_img, 0.4)
normal_btn = button.Button(440, 145, normal_img, 0.4)
planta_btn = button.Button(570, 145, planta_img, 0.4)
psiquico_btm = button.Button(710, 145, psiquico_img, 0.4)
roca_btn = button.Button(850, 145, roca_img, 0.4)
siniestro_btn = button.Button(20, 280, siniestro_img, 0.4)
tierra_btn = button.Button(150, 280, tiera_img, 0.4)
veneno_btn = button.Button(300, 280, veneno_img, 0.4)
volador_btn = button.Button(440, 280, volador_img, 0.4)
primera_gen_btn = button.Button(570, 280, primera_gen_img, 0.8)
segunda_gen_btn = button.Button(760, 280, segunda_gen_img, 0.8)
tercera_gen_btn = button.Button(20, 425, tercera_gen_img, 0.8)
cuarta_gen_btn = button.Button(220, 425, cuarta_gen_img, 0.8)
quinta_gen_btn = button.Button(420, 425, quinta_gen_img, 0.8)
sexta_gen_btn = button.Button(620, 425, sexta_gen_img, 0.8)
filter_btn = button.Button(850, 690, filter_img, 0.5)
back_button = button.Button(50, 700, back_img, 1)

text="< ATK <"
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
clock = pygame.time.Clock()
def show_filters():
  filter_list.clear()
  
  attack = 10
  attack2 = 100
  
  menu_state = "filters"
  screen.fill(TEXT_COL)
  while True:
    mensaje = font.render(str(attack), 1, (0, 0, 0))
    mensaje2 = font.render(str(attack2), 1, (0, 0, 0))
    mensaje3 = font.render(text, 1, (0, 0, 0))
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
      if pygame.key.get_pressed()[K_RIGHT]:
        
        attack += 1
        
      if pygame.key.get_pressed()[K_LEFT]:
         
        attack -= 1
      if pygame.key.get_pressed()[K_UP]:
        
        attack2 += 1
      if pygame.key.get_pressed()[K_DOWN]:
        
        attack2 -= 1
    pygame.display.update()
    screen.fill(TEXT_COL) 
   
    if menu_state == "filters":
        #draw the different filtros buttons
        if bicho_btn.draw(screen):
          type_data={'type':'Bug'}
          if type_data not in filter_list:
            add_filter(type_data)
        if dragon_btn.draw(screen):
          type_data={'type':'Dragon'}
          if type_data not in filter_list:
            add_filter(type_data)
        if electrico_btn.draw(screen):
          type_data={'type':'Electric'}
          if type_data not in filter_list:
            add_filter(type_data)
        if agua_btn.draw(screen):
          type_data={'type':'Water'}
          if type_data not in filter_list:
            add_filter(type_data)
        if fantasma_btn.draw(screen):
          type_data={'type':'Ghost'}
          if type_data not in filter_list:
            add_filter(type_data)
        if fuego_btn.draw(screen):
          type_data={'type':'Fire'}
          if type_data not in filter_list:
            add_filter(type_data)
        if hada_btn.draw(screen):
          type_data={'type':'Fairy'}
          if type_data not in filter_list:
            add_filter(type_data)
        if hielo_btn.draw(screen):
          type_data={'type':'Ice'}
          if type_data not in filter_list:
            add_filter(type_data)
        if lucha_btn.draw(screen):
          type_data={'type':'Fighting'}
          if type_data not in filter_list:
            add_filter(type_data)
        if metal_btn.draw(screen):
          type_data={'type':'Steel'}
          if type_data not in filter_list:
            add_filter(type_data)
        if normal_btn.draw(screen):
          type_data={'type':'Normal'}
          if type_data not in filter_list:
            add_filter(type_data)
        if planta_btn.draw(screen):
          type_data={'type':'Grass'}
          if type_data not in filter_list:
            add_filter(type_data)
        if psiquico_btm.draw(screen):
          type_data={'type':'Psychic'}
          if type_data not in filter_list:
            add_filter(type_data)
        if roca_btn.draw(screen):
          type_data={'type':'Rock'}
          if type_data not in filter_list:
            add_filter(type_data)
        if siniestro_btn.draw(screen):
          type_data={'type':'Dark'}
          if type_data not in filter_list:
            add_filter(type_data)
        if tierra_btn.draw(screen):
          type_data={'type':'Ground'}
          if type_data not in filter_list:
            add_filter(type_data)
        if veneno_btn.draw(screen):
          type_data={'type':'Poison'}
          if type_data not in filter_list:
            add_filter(type_data)
        if volador_btn.draw(screen):
          type_data={'type':'Flying'}
          if type_data not in filter_list:
            add_filter(type_data)
        if primera_gen_btn.draw(screen):
          type_data={'gen':'1'}
          if type_data not in filter_list:
            add_filter(type_data)
        if segunda_gen_btn.draw(screen):
          type_data={'gen':'2'}
          if type_data not in filter_list:
            add_filter(type_data)
        if tercera_gen_btn.draw(screen):
          type_data={'gen':'3'}
          if type_data not in filter_list:
            add_filter(type_data)
        if cuarta_gen_btn.draw(screen):
          type_data={'gen':'4'}
          if type_data not in filter_list:
            add_filter(type_data)
        if quinta_gen_btn.draw(screen):
          type_data={'gen':'5'}
          if type_data not in filter_list:
            add_filter(type_data)
        if sexta_gen_btn.draw(screen):
          type_data={'gen':'6'}
          if type_data not in filter_list:
            add_filter(type_data)
        if filter_btn.draw(screen):
          attack_menor={'attack_menor':int(attack)}
          add_filter(attack_menor)
          attack_mayor={'attack_mayor':int(attack2)}
          add_filter(attack_mayor)
          listado.list_main(filter_list)
        if back_button.draw(screen):
          listado.list_main(filter_list)

       
        screen.blit(mensaje, (250, 600))
        screen.blit(mensaje3, (350, 600))
        screen.blit(mensaje2, (600, 600))
        pygame.display.update()
        pygame.display.flip()
         
    pygame.display.update()

################################################################################

#show_filters()

################################################################################    