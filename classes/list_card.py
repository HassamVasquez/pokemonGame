import pygame
from classes.button import Button


class ListCard(Button):
    def __init__(self, x:int, y:int) -> None:
        # Load background card list image
        background_image = pygame.image.load('images/cards/card_background_yellow.png').convert_alpha()
        super().__init__(x, y, background_image)
