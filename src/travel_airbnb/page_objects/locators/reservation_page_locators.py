from .base_locators import BaseLocators

class ReservationPageLocators(BaseLocators):
    # Fixed locators
    RESERVE_BTN = BaseLocators.css('div[class="_fz3zdn"] > div > button[data-testid="homes-pdp-cta-btn"]')
    SHOW_ALL_AMENITIES_BTN = BaseLocators.xpath('//button[contains(text(), "Show all") and contains(text(), "amenities")]')
    AMENITY_LIST =  BaseLocators.css('div[class="_11jhslp"] ul > li')
    CLOSE_AMENITIES_BTN = BaseLocators.css('div[data-testid="modal-container"] button')
    PRICE_DISPLAY = BaseLocators.css('span[class="_11jcbg2"]')[1]