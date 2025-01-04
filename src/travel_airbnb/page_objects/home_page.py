from typing import Tuple
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .properties_result_page import PropertiesResultPage
from .locators.home_page_locators import HomePageLocators
from src.travel_airbnb.utils.enums import GuestType
from src.core.factories.page_factory import PageFactory

class HomePage(BasePage):
    def wait_for_page_load(self):
        pass

    def select_currency(self, currency: str) -> None:
        # Click 'Language and Currency' button
        self.find_element_and_click(HomePageLocators.LANGUAGE_CURRENCY_BTN)
        # Select currency tab
        self.find_element_and_click(HomePageLocators.CURRENCY_TAB)
        # Select the desired currency
        currency_option = HomePageLocators.get_currency_option(currency)
        self.find_element_and_click(currency_option)
        # Wait for the currency option pop up to disappear
        self.wait_for_element_to_disappear(currency_option)

    def confirm_current_currency(self) -> str:
        # Retrieve currently selected currency for assertions
        currency_displays = self.find_elements(HomePageLocators.CURRENCY_RESULT)
        return currency_displays[1].text
    
    def select_destination(self, destination: str) -> None:
        # Enter the destination
        element = self.wait_for_element_and_send_keys(
            HomePageLocators.DESTINATION_INPUT,
            destination,
            EC.element_to_be_clickable)
        # Wait for and choose the autocompleted result
        self.wait_for_element_and_click(
            HomePageLocators.DESTINATION_AUTOCOMPLETE_RESULT,
            EC.text_to_be_present_in_element,
            destination.capitalize())

    def confirm_destination(self) -> str:
        # Retrieve choosen destination for assertion
        return self.find_element_and_get_attribute(
            HomePageLocators.DESTINATION_INPUT, 'value')

    def add_checkin_and_checkout_dates(
            self, 
            checkin_date: str, 
            checkout_date: str) -> None:
        self.find_element_and_click(HomePageLocators.get_date_locator(checkin_date))
        self.find_element_and_click(HomePageLocators.get_date_locator(checkout_date))

    def confirm_checkin_and_checkout_dates(self) -> Tuple[str, str]:
        checkin_date = self.find_element_and_get_text(HomePageLocators.CHECKIN_DATE)
        checkout_date = self.find_element_and_get_text(HomePageLocators.CHECKOUT_DATE)
        return checkin_date, checkout_date

    def add_guests(
        self,
        adults: int = 1,
        children: int = 0,
        infants: int = 0,
        pets: int = 0):
        self.find_element_and_click(HomePageLocators.GUESTS_BTN)
        if adults > 0:
            self._increment_guest_count(adults, GuestType.ADULTS.value)
        if children > 0:
            self._increment_guest_count(children, GuestType.CHILDREN.value)
        if infants > 0:
            self._increment_guest_count(infants, GuestType.INFANTS.value)
        if pets > 0:
            self._increment_guest_count(pets, GuestType.PETS.value)

    def _increment_guest_count(self, count: int, guest_type: str) -> None:
        guest_button = HomePageLocators.get_guest_type_button(guest_type)
        for _ in range(count):
            self.find_element_and_click(guest_button)

    def confirm_guests(self) -> str:
        guests = self.find_element_and_get_text(HomePageLocators.GUESTS_BTN)
        return guests.split('\n')[1]

    def search_and_get_result_page(self) -> PropertiesResultPage:
        self.find_element_and_click(HomePageLocators.SEARCH_BTN)
        return PageFactory.create_page(self.driver, PropertiesResultPage)
