from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
	
	def should_be_basket_is_empty(self):
		assert "empty" in self.browser.find_element(*BasePageLocators.BASKET_EMPTY).text, "basket is not empty"
	