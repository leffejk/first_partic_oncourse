import pytest; from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser): # Обработчик функции language
    parser.addoption('--language', action='store', default='en', 
                     help="Please select a language")

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("language")
    if language:
        options = Options() # Создаем опцию
        options.add_experimental_option('prefs', {'intl.accept_languages': language}) # Добавляем в нее выбор языка
        print('\n- Запуск браузера -') 
        browser = webdriver.Chrome(options=options) # Запускаем Chrome с этой опцией
    else:
        raise pytest.UsageError("--language=[Введите язык]")
    yield browser
    print('\n- Закрытие браузера -')
    browser.quit()