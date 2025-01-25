from .base_locators import BaseLocators

class PaymentAndReservationPageLocators(BaseLocators):
    PAYMENT_METHOD_DROPDOWN = BaseLocators.id('dropdown-selector-payment_option_selector-button')
    PAYMENT_METHOD_DROPDOWN_OPTIONS = BaseLocators.css('ul[id="dropdown-selector-payment_option_selector-options"] li')
    CARD_NUMBER_INPUT = BaseLocators.css('input[name="credit-card-number"]')
    EXPIRATION_INPUT = BaseLocators.css('input[name="credit-card-expiration"]')
    CVV_INPUT = BaseLocators.css('input[name="credit-card-cvv"]')
    ZIP_CODE_INPUT = BaseLocators.css('input[name="zipCode"]')
    REQUESTTOBOOK_BTN = BaseLocators.css('div[data-testid="submit-button"] > button')