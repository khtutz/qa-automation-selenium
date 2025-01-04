from typing import Self
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators.signup_login_page_locators import SignupLoginPageLocators
from src.core.factories.page_factory import PageFactory

class LoginPage(BasePage):
    def navigate(self) -> Self:
        self.driver.get(self.config.login_url)
        return self

    def wait_for_page_load(self):
        pass

    def continue_with_email(self, email: str) -> Self:
        # Click 'Continue with Email' button
        self.wait_for_element_and_click(
            SignupLoginPageLocators.EMAIL_BTN,
            EC.element_to_be_clickable)
        # Enter email and click 'Continue' button
        self.wait_for_element_and_send_keys(
            SignupLoginPageLocators.EMAIL_INPUT, 
            email)
        self.find_element_and_click(SignupLoginPageLocators.CONTINUE_BTN)
        return self

    def login_with_password(self, password: str) -> None:
        self.wait_for_element_and_send_keys(
            SignupLoginPageLocators.PASSWORD_INPUT,
            password)
        self.find_element_and_click(SignupLoginPageLocators.LOGIN_BTN)

    def confirm_login(self) -> bool:
        return self.is_user_logged_in(
            SignupLoginPageLocators.PROFILE_IMG,
            EC.presence_of_element_located)
