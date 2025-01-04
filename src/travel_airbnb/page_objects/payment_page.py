from typing import Tuple, Optional, Self
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators.payment_page_locators import PaymentPageLocators
from src.core.factories.page_factory import PageFactory

class PaymentPage(BasePage):
    def wait_for_page_load(self, driver):
        pass
