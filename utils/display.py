import pygame


from definitions import colours as COLOURS

from pygame.locals import *

def changeTamDisplay(x,y):
    game_width = x
    game_height = y
    size = (game_width, game_height)
    game = pygame.display.set_mode(size)

def create_button(width, height, left, top, text_cx, text_cy, label,game_screen):

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
def display_message(game_screen: pygame.Surface, message):
    pygame.draw.rect(game_screen, COLOURS.WHITE, (10, 350, 480, 140))
    pygame.draw.rect(game_screen, COLOURS.BLACK, (10, 350, 480, 140), 3)
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render(message, True, COLOURS.BLACK)
    text_rect = text.get_rect()
    text_rect.x = 30
    text_rect.y = 410
    game_screen.blit(text, text_rect)
    pygame.display.update()

def drawBatlle(player_pokemon,rival_pokemon,game_screen: pygame.Surface ):
        game_screen.fill(COLOURS.WHITE)
        player_pokemon.draw(game_screen)
        rival_pokemon.draw(game_screen)
        player_pokemon.draw_hp(game_screen)
        rival_pokemon.draw_hp(game_screen)
        