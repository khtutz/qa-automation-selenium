from .base_page import BasePage
from .locators.pay_and_reserve_page_locators import PaymentAndReservationPageLocators

class PaymentAndReservationPage(BasePage):
    def wait_for_page_load(self):
        pass

    def fill_up_payment_details(
        self,
        card_number: str,
        expiry_date: str,
        cvv: str,
        zip_code: str) -> None:
        # Select credit/debit card option from drop down menu
        self.find_element_and_click(
            PaymentAndReservationPageLocators.PAYMENT_METHOD_DROPDOWN)
        self.find_elements_and_click_nth_element(
            PaymentAndReservationPageLocators.PAYMENT_METHOD_DROPDOWN_OPTIONS, 
            0)
        
        # Enter card details: card number, expiration date, and CVV
        self.find_element_and_send_keys(
            PaymentAndReservationPageLocators.CARD_NUMBER_INPUT, card_number)
        self.find_element_and_send_keys(
            PaymentAndReservationPageLocators.EXPIRATION_INPUT, expiry_date)
        self.find_element_and_send_keys(
            PaymentAndReservationPageLocators.CVV_INPUT, cvv)

        # Enter zip code
        self.find_element_and_send_keys(
            PaymentAndReservationPageLocators.ZIP_CODE_INPUT, zip_code)

    def confirm_and_pay(self):
        pass
        # Following is commented out to prevent from actual booking
        #self.find_element_and_click(PaymentAndReservationPageLocators.REQUESTTOBOOK_BTN)