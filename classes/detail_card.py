import pygame

import definitions.colours as COLOURS

from classes.action_button import ActionButton
from classes.pokemon import Pokemon


class DetailCard():
    def __init__(self) -> None:

        # Bakcground pokemon details
        self.details_background = pygame.Surface((1280, 720))
        self.details_background.set_alpha(220)
        self.details_background.fill(COLOURS.BLACK)

        # Details Card
        self.details_card_background = pygame.Surface((500, 680))
        self.details_card_background.fill(COLOURS.WHITE)

        # Buttons
        button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()
        self.close_button = ActionButton(512, 660, button_background, 'CLOSE', hover_scale=1.08)
        self.fight_button = ActionButton(768, 660, button_background, 'FIGHT', hover_scale=1.08)


    
    
    def draw(self, screen: pygame.Surface, pokemon: Pokemon, showing_details: list[bool]):
        print(pokemon.name)
        # Translucent background
        screen.blit(self.details_background, (0, 0))

        # Background details card
        dcb_rect = self.details_card_background.get_rect()
        dcb_rect.center = (640, 360)
        screen.blit(self.details_card_background, dcb_rect.topleft)

        # Close button
        if self.close_button.draw(screen):
            showing_details[0] = False
            
        # Fight button
        if self.fight_button.draw(screen):
            showing_details[0] = False
            print('Peleaaaaar')