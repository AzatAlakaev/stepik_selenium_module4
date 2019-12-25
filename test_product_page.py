from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time
import pytest

xfail = pytest.mark.xfail

class TestUserAddToBasketFromProductPage():

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
	#открыть страницу регистрации
		link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		page = LoginPage(browser, link)
		page.open() 
    #зарегистрировать нового пользователя
		email = str(time.time()) + "@fakemail.org"
		password = "strongPassword"
		page.register_new_user(email, password)
	#проверить, что пользователь залогинен
		page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
		page = ProductPage(browser, link)
		page.open() 
		page.should_not_be_success_message()
	
	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
		page = ProductPage(browser, link)
		page.open()
		page.add_to_basket()
		time.sleep(3)
		page.should_be_basket_item()
		page.should_be_basket_sum()
		page.should_be_equals_names_of_book()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
								  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)  
	page.open()                     
	page.add_to_basket()
	time.sleep(3)
	page.should_be_basket_item()
	page.should_be_basket_sum()
	page.should_be_equals_names_of_book()
	
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	#Гость открывает страницу товара
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
	#Переходит в корзину по кнопке в шапке 
    page.go_to_basket_page()
    time.sleep(1)
	#Ожидаем, что в корзине нет товаров
	#Ожидаем, что есть текст о том что корзина пуста 
    page.should_be_basket_is_empty()
	
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open() 
	page.add_to_basket()
	page.should_not_be_success_message()

@xfail	
def test_message_disappeared_after_adding_product_to_basket(browser): 
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)
	page.open() 
	page.add_to_basket()
	page.should_success_message_is_disappeared()