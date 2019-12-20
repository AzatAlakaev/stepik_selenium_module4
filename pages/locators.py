from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators () :
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators () :
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BASKET_ITEM = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in  .alertinner strong")
	BASKET_SUM = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in  .alertinner strong")
	BASKET_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	NAME_OF_BOOK = (By.CSS_SELECTOR, ".alertinner strong")
	BOOKS_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")