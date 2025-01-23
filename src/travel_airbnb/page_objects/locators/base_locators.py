from src.core.page_objects.base_locators import CoreBaseLocators

# To implement shared element locators
class BaseLocators(CoreBaseLocators):
    # Variables for fixed element selector
    POPUP_CLOSE_BTN = CoreBaseLocators.css('div[role="dialog"] button[aria-label="Close"]')
    