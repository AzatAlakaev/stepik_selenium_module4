from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.BASKET_ITEM), \
											"Success message is presented, but should not be"
	
	def should_success_message_is_disappeared(self):
		assert self.is_disappeared(*ProductPageLocators.BASKET_ITEM), \
									"Success message is presented, but should not be"
	
	def should_be_basket_button(self):
		assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "basket button is not presented"
	
	def add_to_basket(self):
		#self.browser.find_element_by_css_selector(".btn-add-to-basket").click()
		self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()
		self.solve_quiz_and_get_code()
		
	def should_be_basket_item(self):
		assert self.is_element_present(*ProductPageLocators.BASKET_ITEM), "basket item is not presented"
	
	def should_be_basket_sum(self):
		assert self.browser.find_element(*ProductPageLocators.BASKET_SUM).text \
										== self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text \
										, "it's wrong, sum don't equals price"
	
	def should_be_equals_names_of_book(self):
		assert self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text \
										== self.browser.find_element(*ProductPageLocators.BOOKS_NAME).text \
										, "it's wrong, book names are doesn't equals"
	