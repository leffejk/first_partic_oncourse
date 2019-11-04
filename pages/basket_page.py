from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def clear_cart_chech(self):
        assert self.is_element_present(*BasketLocators.BASKET_CLEAR_ELEMENT), "Корзина не пуста"

    def check_for_not_items_in_the_cart(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_PRODUCTS), "Товары в корзине присутствуют"