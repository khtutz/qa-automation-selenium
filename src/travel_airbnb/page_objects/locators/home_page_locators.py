from .base_locators import BaseLocators
from selenium.webdriver.common.by import By
from typing import Tuple, Union

class HomePageLocators(BaseLocators):
    # Variables for fixed element selector
    LANGUAGE_CURRENCY_BTN = BaseLocators.css('button[aria-label="Choose a language and currency"]')
    CURRENCY_TAB = BaseLocators.css('button[id="tab--language_region_and_currency--1"]')
    CURRENCY_RESULT = BaseLocators.xpath('//span[@class="l120a03b atm_cs_10d11i2 atm_rd_8stvzk_1nos8r dir dir-ltr"]')
    DESTINATION_INPUT = BaseLocators.css('input[data-testid="structured-search-input-field-query"]')
    DESTINATION_AUTOCOMPLETE_RESULT = BaseLocators.css('div[data-index="0"] div:nth-child(2) div')
    CHECKIN_DATE = BaseLocators.css('div[data-testid="structured-search-input-field-split-dates-0"] div div:nth-child(2)')
    CHECKOUT_DATE = BaseLocators.css('div[data-testid="structured-search-input-field-split-dates-1"] div div:nth-child(2)')
    GUESTS_BTN = BaseLocators.css('div[data-testid="structured-search-input-field-guests-button"]')
    SEARCH_BTN = BaseLocators.css('button[data-testid="structured-search-input-search-button"]')

    # Methods for dynamic locators
    @classmethod
    def get_currency_option(cls, currency: str) -> Tuple[Union[By, str], str]:
        xpath = f'//li[.//div[text()="{currency}"]]' 
        return cls.xpath(xpath)

    @classmethod
    def get_date_locator(cls, date: str) -> Tuple[Union[By, str], str]:
        css_selector = f'div[data-testid="{date}"]'
        return cls.css(css_selector)

    @classmethod
    def get_guest_type_button(cls, guest_type: str) -> Tuple[Union[By, str], str]:
        css_selector = f'button[data-testid="stepper-{guest_type}-increase-button"]'
        return cls.css(css_selector)