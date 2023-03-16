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
        self.select_button = ActionButton(768, 660, button_background, 'SELECT', hover_scale=1.08)

        # Info
        self.text_font = pygame.font.SysFont('consolas', 24, bold=True)


    
    
    def draw(self, screen: pygame.Surface, pokemon: Pokemon, selected_pokemon_list: list[Pokemon], showing_details: list[bool]):
        # Translucent background
        screen.blit(self.details_background, (0, 0))

        # Background details card
        dcb_rect = self.details_card_background.get_rect()
        dcb_rect.center = (640, 360)
        screen.blit(self.details_card_background, dcb_rect.topleft)

        # Pokemon image
        pokemon_image = pygame.image.load(f'pokemon_jpg/{pokemon.image_path}').convert_alpha()
        pokemon_image = pygame.transform.scale(pokemon_image, (250, 250))
        pokemon_image_rect = pokemon_image.get_rect()
        pokemon_image_rect.center = (640, 160)
        screen.blit(pokemon_image, pokemon_image_rect.topleft)

        # Info
        name_text = self.text_font.render(pokemon.name, True, COLOURS.BLACK)
        screen.blit(name_text, (550, 300))

        type_1_text = self.text_font.render(pokemon.type_1, True, COLOURS.BLACK)
        screen.blit(type_1_text, (550, 350))

        type_2_text = self.text_font.render(pokemon.type_2, True, COLOURS.BLACK)
        screen.blit(type_2_text, (550, 400))

        generation_text = self.text_font.render(str(pokemon.generation), True, COLOURS.BLACK)
        screen.blit(generation_text, (550, 450))

        # Close button
        if self.close_button.draw(screen):
            showing_details[0] = False
            
        # Select button
        if self.select_button.draw(screen):
            showing_details[0] = False

            # Add selected pokemon to the list
            if not pokemon in selected_pokemon_list and len(selected_pokemon_list) < 3:
                selected_pokemon_list.append(pokemon)
            print(selected_pokemon_list)