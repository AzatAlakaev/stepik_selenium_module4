from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page.open()                      # открываем страницу
	page.add_to_basket()
	time.sleep(3)
	page.should_be_basket_item()
	page.should_be_basket_sum()
	page.should_be_equals_names_of_book()