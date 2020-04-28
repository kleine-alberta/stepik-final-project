from .base_page import BasePage
#from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def click_button_add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_basket.click() 
        
    def should_be_add_to_basket(self):
        Message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        Product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert Message == Product_name, "wrong link"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but should not be"
       
    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
       "Success message is presented, but not disappeared"
       
    
        
       
    

        
        