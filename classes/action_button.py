from classes.button import Button
import pygame
from definitions.colours import WHITE


class ActionButton(Button):
    def __init__(self, x: int, y: int, background: pygame.Surface, text: str, scale: float = 1, hover_scale: float = 1):
        super().__init__(x, y, background, scale)
        width = background.get_width()
        height = background.get_height()

        # button text
        self.text = text

        # hover scale
        self.hover_scale = hover_scale

        # Create diferent views
        self.normal_view: pygame.Surface = self.background_render # detalle
        self.hovered_view: pygame.Surface = pygame.transform.scale(
            background, (int(width * scale * hover_scale), int(height * scale * hover_scale))
        )

        # Text image to render
        self.text_surface = None
    

    def first_action(self):
        # text to render
        font = pygame.font.SysFont('consolas', 34, bold=True)
        self.text_surface = font.render(self.text, True, WHITE)       

    def hovered_button_action(self):
        self.background_render = self.hovered_view
        font = pygame.font.SysFont('consolas', int(34 * self.hover_scale), bold=True)
        self.text_surface = font.render(self.text, True, WHITE)
    
    def hover_button_losed_action(self):
        self.background_render = self.normal_view
    
    def before_bg_drawing_action(self, surface: pygame.Surface):
        self.rect = self.background_render.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
    
    def after_bg_drawing_action(self, surface: pygame.Surface):
        # draw text on button
        text_rect = self.text_surface.get_rect()
        text_rect.center = (self.pos_x, self.pos_y)
        surface.blit(self.text_surface, (text_rect.x, text_rect.y))

