from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "word \"login\" not in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not found"
        
    def register_new_user(self, email, password):
        get_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        get_email.send_keys(email)
        get_password = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        get_password.send_keys(password)
        confirmed = self.browser.find_element(*LoginPageLocators.CONFIRM_PASS)
        confirmed.send_keys(password)
        button = self.browser.find_element_by_css_selector('[name="registration_submit"]')
        button.click()
        assert True, "user  was not autorised"