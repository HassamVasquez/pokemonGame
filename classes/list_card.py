import pygame
from classes.button import Button
from classes.pokemon import Pokemon
import definitions.colours as COLOURS


class ListCard(Button):
    def __init__(self, x:int, y:int, pokemon: Pokemon) -> None:
        # Load background card list image
        background_image = pygame.image.load('images/cards/card_background_yellow.png').convert_alpha()
        super().__init__(x, y, background_image)

        self.pokemon = pokemon
        self.name_surface = pygame.Surface((0, 0))
        self.type_1_surface = pygame.Surface((0, 0))
        self.type_2_surface = pygame.Surface((0, 0))

        # Load pokemon image
        pokemon_image = pygame.image.load(f'pokemon_jpg/{self.pokemon.image_path}').convert_alpha()
        self.pokemon_image = pygame.transform.scale(pokemon_image, (120, 120))
    

    def first_action(self):
        font = pygame.font.SysFont('consolas', 22, bold=True)
        self.name_surface = font.render(self.pokemon.name, True, COLOURS.WHITE)
        self.type_1_surface = font.render(self.pokemon.type_1, True, COLOURS.WHITE)
        self.type_2_surface = font.render(self.pokemon.type_2, True, COLOURS.WHITE)

    
    def after_bg_drawing_action(self, surface: pygame.Surface):
        # Draw name text
        name_rect = self.name_surface.get_rect()
        name_rect.center = (self.pos_x + 69, self.pos_y - 38)
        surface.blit(self.name_surface, name_rect.topleft)

        # Draw type 1 text
        type_1_rect = self.type_1_surface.get_rect()
        type_1_rect.center = (self.pos_x + 69, self.pos_y + 5)
        surface.blit(self.type_1_surface, type_1_rect.topleft)

        # Draw type 2 text
        type_2_rect = self.type_2_surface.get_rect()
        type_2_rect.center = (self.pos_x + 69, self.pos_y + 48)
        surface.blit(self.type_2_surface, type_2_rect.topleft)

        # Draw pokemon image
        pokemon_image_rect = self.pokemon_image.get_rect()
        pokemon_image_rect.center = (self.pos_x - 69, self.pos_y)
        surface.blit(self.pokemon_image, pokemon_image_rect.topleft)
    
