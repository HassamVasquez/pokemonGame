from classes.button import Button
import pygame
from definitions.colours import WHITE


class ActionButton(Button):
    def __init__(self, x: int, y: int, background: pygame.Surface, text: str, scale: float = 1, hover_scale: float = 1, fontTam = 34, changeBgOnDisabled = True):
        super().__init__(x, y, background, scale)
        width = background.get_width()
        height = background.get_height()

        # Disabled Background image to render
        disabled_background = pygame.image.load('images/buttons/grey_button_bg.png').convert_alpha()
        self.disabled_view: pygame.Surface = pygame.transform.scale(
            disabled_background, (int(width * scale), int(height * scale))
        )

        # button text
        self.text = text
        self.font_size: int = int(fontTam * scale)

        # hover scale
        self.hover_scale = hover_scale

        # Create diferent views
        self.normal_view: pygame.Surface = self.background_render # detalle
        self.hovered_view: pygame.Surface = pygame.transform.scale(
            background, (int(width * scale * hover_scale), int(height * scale * hover_scale))
        )

        # Text image to render
        self.text_surface = pygame.Surface((0, 0))

        # Flag
        self.changeBgOnDisabled = changeBgOnDisabled

    def first_action(self, disabled: bool):
        # text to render
        font = pygame.font.SysFont('consolas', self.font_size, bold=True)
        self.text_surface = font.render(self.text, True, WHITE)       

        # Disabled background
        if disabled and self.changeBgOnDisabled:
            self.background_render = self.disabled_view
        else:
            self.background_render = self.normal_view

    def hovered_button_action(self):
        self.background_render = self.hovered_view
        font = pygame.font.SysFont('consolas', int(self.font_size * self.hover_scale), bold=True)
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

