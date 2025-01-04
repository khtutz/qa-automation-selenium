from typing import Tuple
import pytest

from .base_test import BaseTest
from src.core.factories.page_factory import PageFactory
from src.travel_airbnb.page_objects.login_page import LoginPage
from src.core.securities import cookies_helper

class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_login_page(self):
        self.login_page = PageFactory.create_page(self.driver, LoginPage)
        yield

    def test_login(self):
        self.logger.info('-----Start of Login Testing-----')

        # Step 1: Get user credentials, and perform login process
        credentials = self._get_user_credentials()
        login_success: bool = self._perform_login(*credentials)

        # Step 2: Check if login is successful
        assert login_success, 'Login failed'

        # Step 3: Handle session cookies
        if login_success:
            self._handle_session_cookies()

        self.logger.info('-----End of Login Testing-----')

    # Get user credentials from input
    def _get_user_credentials(self) -> Tuple[str, str]:
        email = input('Enter your email: ').strip()
        password = input('Enter your password: ').strip()
        return email, password
    
    # Execute login flow and return success status
    def _perform_login(self, email: str, password: str) -> bool:
        (self.login_page
            .navigate()
            .continue_with_email(email)
            .login_with_password(password))
        
        return self.login_page.confirm_login()
    
    # Handle cookie storage after successful login
    def _handle_session_cookies(self):
        cookies_helper.clear_cookies(
            self.config.login_cookies_path,
            self.logger
        )
        cookies_helper.save_cookies(
            self.driver,
            self.config.login_cookies_path,
            self.logger
        )