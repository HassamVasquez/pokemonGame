import pygame


class ListCard():
    def __init__(self, x:int, y:int) -> None:
        # Load background card list image
        self.image: pygame.Surface = pygame.image.load('images/cards/card_background_yellow.png').convert_alpha()
        #self.image = pygame.transform.scale(self.image, (248, 136))

        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Flags
        self.clicked: bool = False
        self.hovered: bool = False

    def draw(self, surface: pygame.Surface) -> bool:
        action: bool = False

        # Get mouse position
        pos: tuple[int][int] = pygame.mouse.get_pos()

        # Check mouseover
        if self.rect.collidepoint(pos):
            self.hovered = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        else:
            if self.hovered:
                self.hovered = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        # Draw card
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action
