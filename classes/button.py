import pygame
from definitions.colours import WHITE


class Button():
    def __init__(self, x: int, y: int, image: pygame.Surface, text: str, scale: float = 1, hover_scale: float = 1):
        width = image.get_width()
        height = image.get_height()

        # button text
        self.text = text

        # hover scale
        self.hover_scale = hover_scale

        # Create diferent views
        self.image: pygame.Surface = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )
        self.image_hovered: pygame.Surface = pygame.transform.scale(
            image, (int(width * scale * hover_scale), int(height * scale * hover_scale))
        )
        self.image_render = self.image

        # Set position
        self.rect: pygame.Rect = self.image_render.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.rect.center = (self.pos_x, self.pos_y)

        # Flags
        self.clicked: bool = False
        self.hovered: bool = False

    def draw(self, surface: pygame.Surface) -> bool:
        action: bool = False

        # text to render
        font = pygame.font.SysFont('consolas', 34, bold=True)
        text_surface = font.render(self.text, True, WHITE)

        # get mouse position
        pos: tuple[int, int] = pygame.mouse.get_pos()

        # check mouseover (hover)
        if self.rect.collidepoint(pos):
            self.hovered = True
            self.image_render = self.image_hovered
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            font = pygame.font.SysFont('consolas', int(34 * self.hover_scale), bold=True)
            text_surface = font.render(self.text, True, WHITE)

            # check if button is clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            if self.hovered:
                self.hovered = False
                self.image_render = self.image
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        # update rect
        self.rect = self.image_render.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

        # check if mouse is no clicked
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image_render, (self.rect.x, self.rect.y))

        # draw text on button
        rect_text = text_surface.get_rect()
        rect_text.center = (self.pos_x, self.pos_y)
        surface.blit(text_surface, (rect_text.x, rect_text.y))

        return action
