from typing import Tuple, Optional, Self
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators.pay_and_confirm_page_locators import PaymentAndConfirmationPageLocators
from src.core.factories.page_factory import PageFactory

class PaymentAndConfirmationPage(BasePage):
    def wait_for_page_load(self):
        pass
