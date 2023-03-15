import pygame
from math import ceil

from classes.pokemon import Pokemon
from classes.action_button import ActionButton
from classes.list_card import ListCard

from utils.pagination import get_paged_card_list
import definitions.colours as COLOURS


class ListingView():
    def __init__(self) -> None:
        self.page = 0
        self.total_pages = 0
        self.title = None
        self.number_page_font = None
        self.back_button = None
        self.filter_button = None
        self.next_button = None
        self.cards_list = []


    def setup(self, pokemon_list: list[Pokemon]):

        # Pagination page
        self.total_pages = ceil(len(pokemon_list) / 12)

        # VISUAL ELEMENTS

        # Title
        title_font = pygame.font.SysFont('consolas', 60, bold=True)
        self.title = title_font.render('POKEMON LIST', True, COLOURS.BLACK)

        # Number page
        self.number_page_font = pygame.font.SysFont('consolas', 30, bold=True)

        # Load button image
        button_background = pygame.image.load('images/buttons/button_bg_green.png').convert_alpha()

        # Create button instances
        self.back_button = ActionButton(300, 680, button_background, 'BACK', hover_scale=1.08)
        self.filter_button = ActionButton(640, 680, button_background, 'FILTER', hover_scale=1.08)
        self.next_button = ActionButton(980, 680, button_background, 'NEXT', hover_scale=1.08)

        # Create initial cards
        self.cards_list: list[ListCard] = get_paged_card_list(self.page, pokemon_list)


    def loop(self, screen: pygame.Surface, pokemon_list: list[Pokemon]) -> None:

        # Title
        screen.blit(self.title, (440, 5))

        # Number Page
        number_page = self.number_page_font.render(f'Page {self.page + 1} of {self.total_pages} pages', True, COLOURS.BLACK)
        screen.blit(number_page, (480, 600))

        # Back button action
        if self.back_button.draw(screen) and self.page > 0:
            self.page -= 1
            self.cards_list = get_paged_card_list(self.page, pokemon_list)

        # Next button action
        if self.next_button.draw(screen) and self.page < self.total_pages - 1:
            self.page += 1
            self.cards_list = get_paged_card_list(self.page, pokemon_list)

        # Filter button action
        self.filter_button.draw(screen)

        # Pokemon paged list
        clickedCards = [card.draw(screen) for card in self.cards_list]
        # Clicked card
        if any(clickedCards):
            clickedCard = clickedCards.index(True)
            print(f'Se clickeo card {clickedCard}')
