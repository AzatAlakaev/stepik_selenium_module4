from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators () :
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
	REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
	REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
	REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=registration_submit]")

class ProductPageLocators () :
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
	BASKET_ITEM = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in  .alertinner strong")
	BASKET_SUM = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in  .alertinner strong")
	BASKET_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
	NAME_OF_BOOK = (By.CSS_SELECTOR, ".alertinner strong")
	BOOKS_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
	
class BasePageLocators ():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
	BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")