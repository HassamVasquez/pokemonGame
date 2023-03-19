import pygame


class Button():
    # Static state
    button_clicked = False

    def __init__(self, x: int, y: int, background: pygame.Surface, scale: float = 1):
        width = background.get_width()
        height = background.get_height()

        # Background image to render
        self.background_render: pygame.Surface = pygame.transform.scale(
            background, (int(width * scale), int(height * scale))
        )

        # Set position
        self.rect: pygame.Rect = self.background_render.get_rect()
        self.pos_x = x
        self.pos_y = y
        self.rect.center = (self.pos_x, self.pos_y)

        # Flags
        self.hovered: bool = False


    def first_action(self, disabled: bool):
        pass

    def hovered_button_action(self):
        pass

    def hover_button_losed_action(self):
        pass

    def before_bg_drawing_action(self, surface: pygame.Surface):
        pass

    def after_bg_drawing_action(self, surface: pygame.Surface):
        pass

    def draw(self, surface: pygame.Surface, disabled: bool = False, inactive: bool = False) -> bool:
        action: bool = False

        # First Action
        self.first_action(disabled)

        # get mouse position
        pos: tuple[int, int] = pygame.mouse.get_pos()

        # check mouseover (hover)
        if self.rect.collidepoint(pos) and not disabled and not inactive:
            self.hovered = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            self.hovered_button_action()

            # check if button is clicked
            if pygame.mouse.get_pressed()[0] == 1 and not Button.button_clicked and not disabled:
                Button.button_clicked = True
                action = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        else:
            if self.hovered:
                self.hovered = False
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                self.hover_button_losed_action()


        # check if mouse is no clicked
        if pygame.mouse.get_pressed()[0] == 0:
            Button.button_clicked = False
        
        self.before_bg_drawing_action(surface)

        # draw button on screen
        surface.blit(self.background_render, (self.rect.x, self.rect.y))

        self.after_bg_drawing_action(surface)

        return action
