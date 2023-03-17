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
        self.number_page_font = pygame.font.SysFont('consolas', 26, bold=True)

        # Choosed pokemon
        self.choosed_pokemon_text = self.number_page_font.render('Choosed pokemon:', True, COLOURS.BLACK)


        # BUTTONS

        # Load button image
        button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()

        # Button instances
        self.back_button = ActionButton(300, 680, button_background, 'BACK', hover_scale=1.08)
        self.filter_button = ActionButton(640, 680, button_background, 'FILTER', hover_scale=1.08)
        self.next_button = ActionButton(980, 680, button_background, 'NEXT', hover_scale=1.08)

        # Create initial cards
        self.cards_list: list[ListCard] = get_paged_card_list(self.page, pokemon_list)

        # Selected pokemon buttons
        self.selected_pokemon_buttons: list[IconButton] = []


        # POKEMON DETAILS

        self.showing_details: list[bool] = [False]
        self.detail_card = DetailCard()

        self.selected_pokemon: Pokemon = Pokemon()

    def update_selected_pokemon_buttons(self, pokemon_list: list[Pokemon]):
        self.selected_pokemon_buttons = [IconButton(300 + 80 * i, 600, pokemon.image_path) for i, pokemon in enumerate(pokemon_list)]

    def loop(self, screen: pygame.Surface, pokemon_list: list[Pokemon], selected_pokemon_list: list[Pokemon], state: list[GameState]) -> None:

        # Title
        title_rect = self.title.get_rect()
        title_rect.center = (640, 25)
        screen.blit(self.title, title_rect.topleft)

        # Number Page
        number_page = self.number_page_font.render(f'Page {self.page + 1} of {self.total_pages} pages', True, COLOURS.BLACK)
        screen.blit(number_page, (990, 590))

        # Choosed pokemon
        screen.blit(self.choosed_pokemon_text, (30, 590))


        # Back button action
        if self.back_button.draw(screen, self.showing_details[0]) and self.page > 0:
            self.page -= 1
            self.cards_list = get_paged_card_list(self.page, pokemon_list)

        # Next button action
        if self.next_button.draw(screen, self.showing_details[0]) and self.page < self.total_pages - 1:
            self.page += 1
            self.cards_list = get_paged_card_list(self.page, pokemon_list)

        # Filter button action
        if self.filter_button.draw(screen, self.showing_details[0]):
            state[0] = GameState.FILTERING


        # Pokemon paged list
        clickedCards = [card.draw(screen, self.showing_details[0]) for card in self.cards_list]
        # Clicked card
        if any(clickedCards):
            clickedCard = clickedCards.index(True)
            self.selected_pokemon = self.cards_list[clickedCard].pokemon
            self.showing_details[0] = True
        
        # Selected pokemon
        selected_pokemon_clicked = [button.draw(screen) for button in self.selected_pokemon_buttons]
        # Clicked selected pokemon
        if any(selected_pokemon_clicked):
            clicked_pokemon_index = selected_pokemon_clicked.index(True)
            selected_pokemon_list.pop(clicked_pokemon_index)
            self.update_selected_pokemon_buttons(selected_pokemon_list)

        # Pokemon details
        if self.showing_details[0]:
            self.detail_card.draw(screen, self.selected_pokemon, selected_pokemon_list, self.showing_details)
            self.update_selected_pokemon_buttons(selected_pokemon_list)
