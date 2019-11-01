from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_baster(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def message_stating_that_the_item_has_been_added_to_the_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD), "Нет сообщения о добавлении в карзину"

    def product_name_matches_the_name_in_the_message(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message == product_name, "Название товара в сообщении не совпадает с действительным товаром"

    def price_check(self):
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_message == price_product, "Цены не совпадают"


