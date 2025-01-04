from typing import Tuple, Optional, Self
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators.reservation_page_locators import ReservationPageLocators
from src.core.factories.page_factory import PageFactory

class ReservationPage(BasePage):
    def wait_for_page_load(self):
        pass

