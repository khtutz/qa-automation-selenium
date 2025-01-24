from .base_locators import BaseLocators

class PaymentAndConfirmationPageLocators(BaseLocators):
    # Fixed locators
    TOTAL_PRICE_DISPLAY = BaseLocators.css('div[data-testid="price-item-ACCOMMODATION"]')
    DISCOUNT_PRICE_DISPLAY = BaseLocators.css('div[data-testid="price-item-PRICING_RULE_LENGTH_OF_STAY_DISCOUNT"]')
    FINAL_TOTAL_PRICE_DISPLAY = BaseLocators.css('div[data-testid="price-item-total"]')
    PAYMENT_METHODS_SECTION = BaseLocators.css('div[data-testid="payment-methods"]')
    PAYMENT_OPTION_DROPDOWN = BaseLocators.id('dropdown-selector-payment_option_selector-button')
    PAYMENT_OPTION_DROPDOWN_OPTIONS = BaseLocators.css('ul[id="dropdown-selector-payment_option_selector-options"] li')
    CARD_NUMBER_INPUT = BaseLocators.css('input[name="credit-card-number"]')
    EXPIRATION_INPUT = BaseLocators.css('input[name="credit-card-expiration"]')
    CVV_INPUT = BaseLocators.css('input[name="credit-card-cvv"]')
    ZIP_CODE_INPUT = BaseLocators.css('input[name="zipCode"]')
    REQUESTTOBOOK_BTN = BaseLocators.css('div[data-testid="submit-button"] > button')