import pygame
from math import ceil

from classes.pokemon import Pokemon
from classes.action_button import ActionButton
from classes.icon_button import IconButton
from classes.list_card import ListCard
from classes.detail_card import DetailCard

from utils.pagination import get_paged_card_list
import definitions.colours as COLOURS
from definitions.game_state import GameState


class ListingView():
    def __init__(self, pokemon_list: list[Pokemon]) -> None:
        # Pagination
        self.page = 0
        self.total_pages = ceil(len(pokemon_list) / 12)


        # TEXT

        # Title
        title_font = pygame.font.SysFont('consolas', 40, bold=True)
        self.title = title_font.render('POKEMON LIST', True, COLOURS.BLACK)

        # Number page
        self.number_page_font = pygame.font.SysFont('consolas', 22, bold=True)

        # Choosed pokemon
        choosed_pokemon_font = pygame.font.SysFont('consolas', 26, bold=True)
        self.choosed_pokemon_text = choosed_pokemon_font.render('Choosed pokemon:', True, COLOURS.BLACK)

        # Empty pokemon list
        empty_list_font = pygame.font.SysFont('consolas', 32, bold=True)
        self.empty_list_text = empty_list_font.render('*** No Pokemons Found ***', True, COLOURS.BLACK)


        # BUTTONS

        # Load button image
        button_bg_orange = pygame.image.load('images/buttons/orange_button_bg.png').convert_alpha()
        button_bg_blue = pygame.image.load('images/buttons/blue_button_bg.png').convert_alpha()

        # Button instances
        self.filter_button = ActionButton(94, 590, button_bg_orange, 'FILTER', 0.75, 1.08)
        self.back_button = ActionButton(574, 590, button_bg_blue, 'BACK', 0.75, 1.08)
        self.next_button = ActionButton(706, 590, button_bg_blue, 'NEXT', 0.75, 1.08)

        # Create initial cards
        self.cards_list: list[ListCard] = get_paged_card_list(self.page, pokemon_list)

        # Selected pokemon buttons
        self.selected_pokemon_buttons: list[IconButton] = []

        # Figth Button
        button_bg_red = pygame.image.load('images/buttons/red_button_bg.png').convert_alpha()
        self.fight_button = ActionButton(640, 676, button_bg_red, 'FIGTH', hover_scale=1.08)


        # POKEMON DETAILS

        self.showing_details: list[bool] = [False]
        self.detail_card = DetailCard()

        self.selected_pokemon: Pokemon = Pokemon()

    def update_selected_pokemon_buttons(self, pokemon_list: list[Pokemon]):
        self.selected_pokemon_buttons = [IconButton(300 + 80 * i, 676, pokemon.image_path) for i, pokemon in enumerate(pokemon_list)]

    def loop(self, screen: pygame.Surface, pokemon_list: list[Pokemon], selected_pokemon_list: list[Pokemon], state: list[GameState]) -> None:

        # Title
        title_rect = self.title.get_rect()
        title_rect.center = (640, 25)
        screen.blit(self.title, title_rect.topleft)

        # Number Page
        number_page = self.number_page_font.render(f'Page {self.page + 1} of {self.total_pages} pages', True, COLOURS.BLACK)
        screen.blit(number_page, (1015, 580))

        # Choosed pokemon
        screen.blit(self.choosed_pokemon_text, (30, 664))


        # Back button action
        if self.back_button.draw(screen, self.page <= 0, self.showing_details[0]):
            self.page -= 1
            self.cards_list = get_paged_card_list(self.page, pokemon_list)

        # Next button action
        if self.next_button.draw(screen, self.page >= self.total_pages - 1, self.showing_details[0]):
            self.page += 1
            self.cards_list = get_paged_card_list(self.page, pokemon_list)

        # Filter button action
        if self.filter_button.draw(screen, inactive=self.showing_details[0]):
            state[0] = GameState.FILTERING


        # Pokemon paged list
        clickedCards = [card.draw(screen, inactive=self.showing_details[0]) for card in self.cards_list]
        # Clicked card
        if any(clickedCards):
            clickedCard = clickedCards.index(True)
            self.selected_pokemon = self.cards_list[clickedCard].pokemon
            self.showing_details[0] = True
        
        # Empty pokemon list
        if (len(pokemon_list) == 0):
            screen.blit(self.empty_list_text, (420, 280))
        
        # Selected pokemon
        selected_pokemon_clicked = [button.draw(screen, inactive=self.showing_details[0]) for button in self.selected_pokemon_buttons]
        # Clicked selected pokemon
        if any(selected_pokemon_clicked):
            clicked_pokemon_index = selected_pokemon_clicked.index(True)
            selected_pokemon_list.pop(clicked_pokemon_index)
            self.update_selected_pokemon_buttons(selected_pokemon_list)
        
        # Fight Button
        if self.fight_button.draw(screen, len(selected_pokemon_list) in [0, 2], self.showing_details[0]):
            if len(selected_pokemon_list) == 1:
                state[0] = GameState.SINGLE_BATTLE
            else:
                state[0] = GameState.TEAM_BATTLE

        # Pokemon details
        if self.showing_details[0]:
            self.detail_card.draw(screen, self.selected_pokemon, selected_pokemon_list, self.showing_details)
            self.update_selected_pokemon_buttons(selected_pokemon_list)
    
    def update(self, pokemon_list: list[Pokemon]):
        # Pagination
        self.page = 0
        self.total_pages = ceil(len(pokemon_list) / 12)

        # Update initial cards
        self.cards_list: list[ListCard] = get_paged_card_list(self.page, pokemon_list)
