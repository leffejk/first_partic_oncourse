# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 
from selenium.common.exceptions import NoSuchElementException




'''
Для начала сделаем базовую страницу, от которой будут унаследованы 
все остальные классы. В ней мы опишем вспомогательные методы для работы с драйвером.
'''

class BasePage:
	'''Первым делом добавим конструктор — метод, который вызывается, когда мы создаем объект. 
	Конструктор объявляется ключевым словом __init__. В него в качестве параметров мы передаем экземпляр драйвера и url адрес. 
	Внутри конструктора сохраняем эти данные как аттрибуты нашего класса. Получается примерно так: '''
	def __init__(self, browser, url, timeout = 10):
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def open(self):
		self.browser.get(self.url)

	def is_element_present(self, how, what): # как искать (css, id, xpath и тд) и собственно что искать (строку-селектор). 
		# Чтобы перехватывать исключение, нужна конструкция try/except: 
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException: # Если произошло это исключение, то False, иначе True
			return False
		return True