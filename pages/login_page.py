from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        '''Зарегистрировать нового пользователя'''
        self.go_to_login_page()

        self.browser.find_element(*LoginPageLocators.REG_EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PASS1_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASS2_INPUT).send_keys(password)

        self.browser.find_element_by_name(r"registration_submit").click()


    def should_be_login_page(self):
        '''Checks:
        1) "login" in current-url
        2) elements "Login Form" present
        3) elements "Register Form" present'''

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "URL Некорректный"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOG_EMAIL) \
               and self.is_element_present(*LoginPageLocators.LOG_PASS), \
            "Отсутствует форма логина"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_INPUT) \
               and self.is_element_present(*LoginPageLocators.REG_PASS1_INPUT) \
               and self.is_element_present(*LoginPageLocators.REG_PASS2_INPUT), \
            "Отсутствует форма регистрации"