from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert "login" in url, "URL Некорректный"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOG_EMAIL) \
               and self.is_element_present(*LoginPageLocators.LOG_PASS), \
            "Отсутствует форма логина"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_INPUT) \
               and self.is_element_present(*LoginPageLocators.REG_PASS1_INPUT) \
               and self.is_element_present(*LoginPageLocators.REG_PASS2_INPUT), \
            "Отсутствует форма регистрации"