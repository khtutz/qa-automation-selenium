from typing import Tuple, Union
from .base_locators import BaseLocators
from selenium.webdriver.common.by import By

class PropertiesResultPageLocators(BaseLocators):
    # Fixed locators
    FILTERS_BTN = BaseLocators.css('button[data-testid="category-bar-filter-button"]')
    MIN_PRICE_INPUT = BaseLocators.id('price_filter_min')
    MAX_PRICE_INPUT = BaseLocators.id('price_filter_max')
    BEDROOMS_BTN = BaseLocators.css('button[data-testid="stepper-filter-item-min_bedrooms-stepper-increase-button"]')
    BEDS_BTN = BaseLocators.css('button[data-testid="stepper-filter-item-min_beds-stepper-increase-button"]')
    BATHROOMS_BTN = BaseLocators.css('button[data-testid="stepper-filter-item-min_bathrooms-stepper-increase-button"]')
    PROPERTY_TYPE_SECTION = BaseLocators.css('div[id="FILTER_SECTION_CONTAINER:PROPERTY_TYPES_WITH_SUBCATEGORY-row-title"]')
    AMENITIES_SHOW_MORE_BTN = BaseLocators.xpath('//section[div[div[h2[text()="Amenities"]]]]/div/div/div/button')    
    SHOW_FILTERED_PROPERTIES_LINK = BaseLocators.xpath('//a[contains(text(), "Show")]')
    APPLIED_FILTERS_COUNT = BaseLocators.css('button[data-testid="category-bar-filter-button"] + div')
    PROPERTIES_LIST = BaseLocators.css('div[class="dmzfgqv atm_5sauks_glywfm dir dir-ltr"] > div > div')
    PROPERTIES_LIST_FIRST_ITEM = BaseLocators.css('div[class="dmzfgqv atm_5sauks_glywfm dir dir-ltr"] > div > div:first-child')

    # Dynamic locators
    @classmethod
    def get_type_of_place(cls, type_of_place: str) -> Tuple[Union[By, str], str]:
        css_selector = f'div[aria-describedby="room-filter-description-{type_of_place}"]'
        return cls.css(css_selector)
    
    @classmethod
    def get_property_type_selection_btn(cls, property_type: str) -> Tuple[Union[By, str], str]:
        xpath = f'//button/span[contains(text(), "{property_type}")]'
        return cls.xpath(xpath)
    
    @classmethod
    def get_amenity_option(cls, option: str) -> Tuple[Union[By, str], str]:
        xpath = f'//button[span[text()="{option}"]]'
        return cls.xpath(xpath)
    
    @classmethod
    def get_booking_option(cls, option: str) -> Tuple[Union[By, str], str]:
        css_selector = f'button[id="filter-item-{option}"]'
        return cls.css(css_selector)
    
    @classmethod
    def get_property(cls, nth: int) -> Tuple[Union[By, str], str]:
        css_selector = f'div[class="dmzfgqv atm_5sauks_glywfm dir dir-ltr"] > div > div:nth-child({nth}) div[data-testid="card-container"]'
        return cls.css(css_selector)