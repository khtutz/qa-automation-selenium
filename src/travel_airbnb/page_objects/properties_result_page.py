import random
from typing import List, Tuple, Optional, Self

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .locators.properties_result_page_locators import PropertiesResultPageLocators
from src.travel_airbnb.page_objects.confirmation_page import ConfirmationPage
from src.core.factories.page_factory import PageFactory
from src.travel_airbnb.utils.enums import PlaceType

class PropertiesResultPage(BasePage):
    DEFAULT_TYPE_OF_PLACE: str = PlaceType.ANY_TYPE.value
    DEFAULT_MIN_PRICE: int = 10
    DEFAULT_MAX_PRICE: int = 300
    DEFAULT_BEDROOMS_COUNT: int = 0
    DEFAULT_BEDS_COUNT: int = 0
    DEFAULT_BATHROOMS_COUNT: int = 0
    DEFAULT_PROPERTY_TYPE: str = ''
    DEFAULT_AMENITY_OPTIONS: Optional[Tuple[str]] = ()
    DEFAULT_BOOKING_OPTIONS: Optional[Tuple[str]] = ()

    def wait_for_page_load(self):
        pass

    def apply_all_filters(self, **kwargs) -> None:
        self.click_filters_btn()
        self.select_type_of_place(
            kwargs.get('type_of_place', self.DEFAULT_TYPE_OF_PLACE)
        ).select_price_range(
            kwargs.get('min_price', self.DEFAULT_MIN_PRICE),
            kwargs.get('max_price', self.DEFAULT_MAX_PRICE)
        ).select_num_of_rooms_and_beds(
            kwargs.get('bedrooms_count', self.DEFAULT_BEDROOMS_COUNT),
            kwargs.get('beds_count', self.DEFAULT_BEDS_COUNT),
            kwargs.get('bathrooms_count', self.DEFAULT_BATHROOMS_COUNT)
        ).select_property_type(
            kwargs.get('property_type', self.DEFAULT_PROPERTY_TYPE)
        ).select_amenity_options(
            kwargs.get('amenity_options', self.DEFAULT_AMENITY_OPTIONS)
        ).select_booking_options(
            kwargs.get('booking_options', self.DEFAULT_BOOKING_OPTIONS)
        ).display_filtered_properties()

    def click_filters_btn(self) -> None:
        self.wait_for_element_and_click(
            PropertiesResultPageLocators.FILTERS_BTN,
            EC.element_to_be_clickable)

    def select_type_of_place(self, type_of_place: str) -> Self:
        type_of_place_locator = PropertiesResultPageLocators.get_type_of_place(type_of_place)
        self.find_element_and_click(type_of_place_locator)
        return self
    
    def select_price_range(self, min_price: int, max_price: int) -> Self:
        self.find_element_and_send_keys(
            PropertiesResultPageLocators.MIN_PRICE_INPUT,
            min_price,
            clear_input_element=True)
        self.find_element_and_send_keys(
            PropertiesResultPageLocators.MAX_PRICE_INPUT,
            max_price,
            clear_input_element=True)
        return self
        
    def select_num_of_rooms_and_beds(
            self, 
            bedrooms_count: int, 
            beds_count: int, 
            bathrooms_count: int) -> Self:
        if bedrooms_count > 0:
            self.find_element_and_click(
                PropertiesResultPageLocators.BEDROOMS_BTN, 
                action_count=bedrooms_count)
        if beds_count > 0:
            self.find_element_and_click(
                PropertiesResultPageLocators.BEDS_BTN, 
                action_count=beds_count)
        if bathrooms_count > 0:
            self.find_element_and_click(
                PropertiesResultPageLocators.BATHROOMS_BTN, 
                action_count=bathrooms_count)
        return self
    
    def select_property_type(self, property_type: str) -> Self:
        if property_type:
            self.find_element_and_click(PropertiesResultPageLocators.PROPERTY_TYPE_SECTION)
            property_btn_locator = PropertiesResultPageLocators.get_property_type_selection_btn(property_type)
            self.find_element_and_click(property_btn_locator)
        return self
    
    def select_amenity_options(self, amenity_options: Optional[Tuple[str]]) -> Self:
        if amenity_options:
            # Click 'Show More' first to display all amenities
            self.find_element_and_click(PropertiesResultPageLocators.AMENITIES_SHOW_MORE_BTN)
            # Choose amenity option individually
            for option in amenity_options:
                amenity_option_locator = PropertiesResultPageLocators.get_amenity_option(option)
                self.find_element_and_click(amenity_option_locator)
        return self
    
    def select_booking_options(self, booking_options: Optional[Tuple[str]]) -> Self:
        if booking_options:
            # Choose booking option individually
            for option in booking_options:
                booking_option_locator = PropertiesResultPageLocators.get_booking_option(option)
                self.find_element_and_click(booking_option_locator)
        return self
    
    def display_filtered_properties(self) -> None:
        self.find_element_and_click(PropertiesResultPageLocators.SHOW_FILTERED_PROPERTIES_LINK)

    def choose_property_and_get_confirmation_page(self)-> Optional[ConfirmationPage]:
        # Ensure at least one property is displayed
        # If no property is found due to filters, return None
        try:
            self.wait_and_find_element(
                PropertiesResultPageLocators.PROPERTIES_LIST_FIRST_ITEM,
                EC.presence_of_element_located)
        except TimeoutException as e:
            exception_msg = f'No properties found after applying filters. Details: {e}'
            self.logger.error(exception_msg)
            return None
        
        # Choose random property within the filtered list
        properties: List[WebElement] = self.find_elements(
            PropertiesResultPageLocators.PROPERTIES_LIST)
        random_property_index = random.randint(0, len(properties) - 1)
        self.find_element_and_click(
            PropertiesResultPageLocators.get_property(random_property_index))

        return PageFactory.create_page(self.driver, ConfirmationPage)
