from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def check_clear_cart(self):
        '''Проверка, пустая ли корзина'''
        assert self.is_element_present(*BasketLocators.BASKET_CLEAR_ELEMENT), "Корзина не пуста"

    def check_for_not_items_in_the_cart(self):
        '''Проверка, отсутствует ли продукты в корзине'''
        assert self.is_not_element_present(*BasketLocators.BASKET_PRODUCTS), "Товары в корзине присутствуют"