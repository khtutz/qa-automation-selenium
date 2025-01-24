from typing import Tuple, Optional, Self
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators.pay_and_reserve_page_locators import PaymentAndReservationPageLocators
from src.core.factories.page_factory import PageFactory

class PaymentAndReservationPage(BasePage):
    def wait_for_page_load(self):
        pass
