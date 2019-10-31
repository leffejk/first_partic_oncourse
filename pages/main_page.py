''' 
В нем нужно сделать импорт базового класса BasePage: '''
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators # импортируем файл с селекторами
from .login_page import LoginPage

'''
В нем создайте класс  MainPage. Его нужно сделать наследником класса BasePage:'''
class MainPage(BasePage):

	# В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object
	def go_to_login_page(self):
		# Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self.
		# Заодно заменим find на более универсальный:
		link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
		link.click()
		return LoginPage(browser=self.browser, url=self.browser.current_url)


	def should_be_login_link(self):
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK),  "Login link is not presented"