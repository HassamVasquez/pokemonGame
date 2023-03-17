import pygame
from classes.button import Button


class IconButton(Button):
    def __init__(self, x: int, y: int, icon_path:str, scale: float = 1):
        # Selected pokemon background
        background_image = pygame.image.load('images/buttons/square_bg_yellow.png').convert_alpha()
        super().__init__(x, y, background_image, scale)

        # Load pokemon image
        pokemon_image = pygame.image.load(f'pokemon_jpg/{icon_path}').convert_alpha()
        self.pokemon_image = pygame.transform.scale(pokemon_image, (62, 62))

    def after_bg_drawing_action(self, surface: pygame.Surface):
        # Draw pokemon image
        pokemon_image_rect = self.pokemon_image.get_rect()
        pokemon_image_rect.center = (self.pos_x, self.pos_y)
        surface.blit(self.pokemon_image, pokemon_image_rect.topleft)