from selenium.webdriver.common.by import By

class MainPageLocators:
	LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
	REG_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
	REG_PASS1_INPUT = (By.CSS_SELECTOR, '#id_registration-password1')
	REG_PASS2_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')

	LOG_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
	LOG_PASS = (By.CSS_SELECTOR, "#id_login-password")
