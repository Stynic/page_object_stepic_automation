from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        assert get_url == self.url, 'Не тот URL-адрес'

    def should_be_login_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_LINK)
        assert True

    def should_be_register_form(self):
        self.is_element_present(*LoginPageLocators.LOGIN_LINK)
        assert True