from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def check_that_there_is_no_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), 'Элемент присутствует на странице.'


    def verify_that_there_is_no_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD), "Элемент не исчезает"



    def add_to_basket(self):
        '''Add To Basket'''
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def message_stating_that_the_item_has_been_added_to_the_cart(self):
        '''Presence check for Message'''
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD), "Нет сообщения о добавлении в карзину"

    def product_name_matches_the_name_in_the_message(self):
        '''Check, does the product name match the actual'''
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message == product_name, "Название товара в сообщении не совпадает с действительным товаром"

    def price_check(self):
        '''Check, do prices match'''
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_message == price_product, "Цены не совпадают"


