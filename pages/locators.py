from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR,"[name='registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASS = (By.CSS_SELECTOR, "[name='registration-password2']")
    
class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"div.alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.row p.price_color")
    
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_MASSEGE = (By.CSS_SELECTOR, "div.alert-info div.alertinner")
    
    

