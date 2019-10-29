''' 
В нем нужно сделать импорт базового класса BasePage: '''
from .base_page import BasePage
from selenium.webdriver.common.by import By

'''
В нем создайте класс  MainPage. Его нужно сделать наследником класса BasePage:'''
class MainPage(BasePage):

	# В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object
	def go_to_login_page(self):
		# Так как браузер у нас хранится как аргумент класса BasePage, обращаться к нему нужно соответствующим образом с помощью self.
		# Заодно заменим find на более универсальный: 
		link = self.browser.find_element(By.CSS_SELECTOR ,"#login_link")
		link.click() 


	def should_be_login_link(self):
		assert self.is_element_present(By.CSS_SELECTOR, "#login_link"),  "Login link is not presented"