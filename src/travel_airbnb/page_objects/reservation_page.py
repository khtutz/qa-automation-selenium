import re
from typing import List

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators.reservation_page_locators import ReservationPageLocators
from src.core.factories.page_factory import PageFactory
from src.travel_airbnb.page_objects.pay_and_confirm_page import PaymentAndConfirmationPage

class ReservationPage(BasePage):
    def wait_for_page_load(self):
        pass

    def confirm_price_per_night(self) -> float:
        try:
            price_display: WebElement = self.find_elements(ReservationPageLocators.PRICE_DISPLAY)[1]
            price_number: str = re.sub(r'[^\d.]', '', price_display.text)  # Remove non-digit characters except '.'
            price: float = float(price_number)
            return price
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Error occurred while finding price display with locator {ReservationPageLocators.PRICE_DISPLAY}: {e}')
            raise
        except ValueError as e:
            error_msg: str = f'\nInvalid price value: {price_number}\nDetails: {e}'
            self.logger.error(error_msg)
            raise ValueError(error_msg)

    def confirm_amenities(self) -> tuple[str, ...]:
        try:
            self.show_all_amenities()
            amenities: List[WebElement] = self.find_elements(ReservationPageLocators.AMENITY_LIST)
            amenities_names: tuple[str, ...] = (amenity.text for amenity in amenities)
            self.close_show_all_amenities()
            return amenities_names
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Error occurred while finding amenities with locator {ReservationPageLocators.AMENITY_LIST}: {e}')
            raise

    def show_all_amenities(self) -> None:
        self.find_element_and_click(ReservationPageLocators.SHOW_ALL_AMENITIES_BTN)

    def close_show_all_amenities(self) -> None:
        self.find_element_and_click(ReservationPageLocators.CLOSE_AMENITIES_BTN)

    def reserve_and_get_payment_and_confirmation_page(self) -> PaymentAndConfirmationPage:
        self.find_element_and_click(ReservationPageLocators.RESERVE_BTN)
        return PageFactory.create_page(
            self.driver,
            PaymentAndConfirmationPage)