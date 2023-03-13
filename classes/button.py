import pygame


class Button():
    def __init__(self, x: int, y: int, image: pygame.Surface, scale: float):
        width = image.get_width()
        height = image.get_height()

        self.image: pygame.Surface = pygame.transform.scale(
            image, (int(width * scale), int(height * scale))
        )

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.clicked: bool = False

    def draw(self, surface: pygame.Surface) -> bool:
        action: bool = False

        # get mouse position
        pos: tuple[int, int] = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        # check if mouse is no clicked
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
