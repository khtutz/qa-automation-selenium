from typing import Tuple, Optional, Self
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import re

from .base_page import BasePage
from .locators.reservation_page_locators import ReservationPageLocators
from src.core.factories.page_factory import PageFactory

class ReservationPage(BasePage):
    def wait_for_page_load(self):
        pass

    def confirm_price_per_night(self) -> float:
        try:
            price_display = self.wait_and_find_element(ReservationPageLocators.PRICE_DISPLAY)
            price_number = re.sub(r'[^\d.]', '', price_display.text)  # Remove non-digit characters except '.'
            price = float(price_number)
            return price
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Error occurred while finding price display with locator {ReservationPageLocators.PRICE_DISPLAY}: {e}')
            raise
        except ValueError as e:
            self.logger.error(f'Invalid price value: {price_number}')
            raise ValueError(f"Invalid price value: {price_number}") from e

    def confirm_amenities(self):
        try:
            self.show_all_amenities()
            amenities = self.find_elements(ReservationPageLocators.AMENITY_LIST)
            amenities_names = [amenity.text for amenity in amenities]
            self.close_show_all_amenities()
            return amenities_names
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Error occurred while finding amenities with locator {ReservationPageLocators.AMENITY_LIST}: {e}')
            raise

    def show_all_amenities(self):
        self.find_element_and_click(ReservationPageLocators.SHOW_ALL_AMENITIES_BTN)

    def close_show_all_amenities(self):
        self.find_element_and_click(ReservationPageLocators.CLOSE_AMENITIES_BTN)

    def reserve_and_get_payment_and_confirmation_page(self):
        return PageFactory.create_page(
            self.driver,
            PaymentAndConfirmationPage)