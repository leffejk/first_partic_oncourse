from .base_page import BasePage


class MainPage(BasePage):
	''' Конструктор ниже с ключевым словом super на самом деле только вызывает конструктор класса
	    предка и передает ему все те аргументы, которые мы передали в конструктор MainPage. '''
	'''В классе MainPage у нас не осталось никаких методов, поэтому добавим туда заглушку: '''
	def __init__(self, *args, **kwargs):
		super(MainPage, self).__init__(*args, **kwargs)
