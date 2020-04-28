from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_goods_at_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
       "Goods is presented, but should not be"
       
    def should_be_empty_message(self):
        assert self.is_disappeared(*BasketPageLocators.EMPTY_MASSEGE), \
       "Empty message is presented, but not disappeared"
