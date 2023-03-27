import pygame

import definitions.colours as COLOURS

from classes.action_button import ActionButton
from classes.icon_button import IconButton
from classes.pokemon import Pokemon


class DetailCard():
    def __init__(self) -> None:
        # Bakcground pokemon details
        self.details_background = pygame.Surface((1280, 720))
        self.details_background.set_alpha(220)
        self.details_background.fill(COLOURS.BLACK)

        # Details Card
        self.details_card_background = pygame.Surface((0, 0))

        # Buttons
        button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()
        self.close_button = ActionButton(512, 640, button_background, 'CLOSE', 0.9, 1.08)
        self.select_button = ActionButton(768, 640, button_background, 'SELECT', 0.9, 1.08)

        # Info
        # Info
        self.name_font = pygame.font.SysFont('consolas', 28, bold=True)
        self.text_font = pygame.font.SysFont('consolas', 26, bold=True)
    
    
    def draw(self, screen: pygame.Surface, pokemon: Pokemon, selected_pokemon_list: list[Pokemon], showing_details: list[bool]):
        # Translucent background
        screen.blit(self.details_background, (0, 0))

        # Background details card
        self.details_card_background = pygame.image.load(f'images/cards/{pokemon.type_1}.png')
        dcb_rect = self.details_card_background.get_rect()
        dcb_rect.center = (640, 360)
        screen.blit(self.details_card_background, dcb_rect.topleft)

        # Pokemon image
        pokemon_image = pygame.image.load(f'pokemon_images/{pokemon.image_path}').convert_alpha()
        pokemon_image = pygame.transform.scale(pokemon_image, (250, 250))
        pokemon_image_rect = pokemon_image.get_rect()
        pokemon_image_rect.center = (640, 235)
        screen.blit(pokemon_image, pokemon_image_rect.topleft)

        # Info
        name_text = self.name_font.render(pokemon.name, True, COLOURS.BLACK)
        screen.blit(name_text, (422, 50))

        attack_text = self.text_font.render(str(pokemon.attack), True, COLOURS.BLACK)
        attack_text_rect = attack_text.get_rect()
        attack_text_rect.midright  = (814, 62)
        screen.blit(attack_text, attack_text_rect.topleft)

        type_1_text = self.text_font.render(pokemon.type_1, True, COLOURS.BLACK)
        type_1_text_rect = type_1_text.get_rect()
        type_1_text_rect.center = (720, 512)
        screen.blit(type_1_text, type_1_text_rect.topleft)

        # Close button
        if self.close_button.draw(screen):
            showing_details[0] = False
            
        # Select button
        if self.select_button.draw(screen, len(selected_pokemon_list) > 2):
            # Add selected pokemon to the list
            if not pokemon in selected_pokemon_list and len(selected_pokemon_list) < 3:
                selected_pokemon_list.append(pokemon)

            showing_details[0] = False
