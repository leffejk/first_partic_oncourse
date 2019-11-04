from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest
from .pages.basket_page import BasketPage

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = r'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.check_for_not_items_in_the_cart()  # Проверка что нет блока с товарами
    page.clear_cart_chech()  # Проверка на чистую корзину




def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = r"http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=r"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"):
    '''
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    '''
    page = ProductPage(browser, link)
    page.open()
    page.add_to_baster()
    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), 'Элемент присутствует на странице.'


def test_guest_cant_see_success_message(browser, link=r"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"):
    '''
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    '''
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.MESSAGE_ADD), 'Элемент присутствует на странице.'

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link=r"http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"):
    '''
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    '''
    page = ProductPage(browser, link)
    page.open()
    page.add_to_baster()
    assert page.is_disappeared(*ProductPageLocators.MESSAGE_ADD), "Элемент не исчезает"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])



def test_guest_can_add_product_to_basket(browser, link):
    try:
        page = ProductPage(browser, link)
        page.open()
        page.add_to_baster()
        page.solve_quiz_and_get_code()
        page.message_stating_that_the_item_has_been_added_to_the_cart()
        page.product_name_matches_the_name_in_the_message()
        page.price_check()
    except:
        assert False, f"ОШИБКА: {link}"



