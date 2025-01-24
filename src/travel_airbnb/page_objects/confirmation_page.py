from typing import List

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement

from .base_page import BasePage
from .locators.confirmation_page_locators import ConfirmationPageLocators
from src.core.factories.page_factory import PageFactory
from src.core.utils.format_helper import get_price_number
from src.travel_airbnb.page_objects.pay_and_reserve_page import PaymentAndReservationPage

class ConfirmationPage(BasePage):
    def wait_for_page_load(self):
        pass

    def confirm_price_per_night(self) -> float:
        try:
            price_display: WebElement = self.find_elements(ConfirmationPageLocators.PRICE_DISPLAY)[1]
            return get_price_number(price_display.text)
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Error occurred while finding price display with locator {ConfirmationPageLocators.PRICE_DISPLAY}: {e}')
            raise
        except ValueError as e:
            error_msg: str = f'\nInvalid price value: {price_number}\nDetails: {e}'
            self.logger.error(error_msg)
            raise ValueError(error_msg)

    def confirm_amenities(self) -> tuple[str, ...]:
        try:
            self.show_all_amenities()
            amenities: List[WebElement] = self.find_elements(ConfirmationPageLocators.AMENITY_LIST)
            amenities_names: tuple[str, ...] = (amenity.text for amenity in amenities)
            self.close_show_all_amenities()
            return amenities_names
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Error occurred while finding amenities with locator {ConfirmationPageLocators.AMENITY_LIST}: {e}')
            raise

    def show_all_amenities(self) -> None:
        self.find_element_and_click(ReservationPageLocators.SHOW_ALL_AMENITIES_BTN)

    def close_show_all_amenities(self) -> None:
        self.find_element_and_click(ReservationPageLocators.CLOSE_AMENITIES_BTN)

    def reserve_and_get_payment_and_reservation_page(self) -> PaymentAndReservationPage:
        self.find_element_and_click(ReservationPageLocators.RESERVE_BTN)
        return PageFactory.create_page(
            self.driver,
            PaymentAndReservationPage)