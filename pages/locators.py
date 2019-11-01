from selenium.webdriver.common.by import By

class MainPageLocators:
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
	REG_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
	REG_PASS1_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
	REG_PASS2_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')

	LOG_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
	LOG_PASS = (By.CSS_SELECTOR, "#id_login-password")

class ProductPageLocators:
	ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	MESSAGE_ADD = (By.CSS_SELECTOR, r".alertinner > strong")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
	MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alertinner > strong")
	PRICE_PRODUCT = (By.CSS_SELECTOR, r'.col-sm-6.product_main > .price_color')
	PRICE_MESSAGE = (By.CSS_SELECTOR, r'[class="alert alert-safe alert-noicon alert-info  fade in"] > .alertinner > p > strong')
