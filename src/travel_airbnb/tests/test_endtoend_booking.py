import pytest
from unittest import mock
from typing import Set

from .base_test import BaseTest
from src.core.factories.page_factory import PageFactory
from src.core.securities import cookies_helper
from src.core.page_objects import popups_handler
from src.travel_airbnb.page_objects.login_page import LoginPage
from src.travel_airbnb.page_objects.home_page import HomePage
from src.travel_airbnb.page_objects.properties_result_page import PropertiesResultPage
from src.travel_airbnb.page_objects.confirmation_page import ConfirmationPage
from src.travel_airbnb.page_objects.pay_and_reserve_page import PaymentAndReservationPage
from src.travel_airbnb.utils.data_loader import DataLoader
from src.travel_airbnb.data.models.booking_models import SearchCriteria, FilterCriteria
from src.travel_airbnb.page_objects.locators.confirmation_page_locators import ConfirmationPageLocators

class TestEndToEndBooking(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_login_page(self):
        self.login_page = PageFactory.create_page(self.driver, LoginPage)
        self.data_loader = DataLoader(environment='development')
        yield

    @pytest.mark.parametrize('scenario', ['scenario1'])
    def test_endtoend(self, scenario: str) -> None:
        self.logger.info('Logging in...')
        self._login()

        self.logger.info('\n***START OF PROPERTY BOOKING TESTING***')

        # Load test data
        search_criteria, filter_criteria = self.data_loader.get_scenario_data(scenario)
        # To load from encrypted data
        payment_data = {
            'card_number': '4111111111111111',
            'expiry_date': '12/24',
            'cvv': '123',
            'zip_code': '123456'
        }

        # Test 1: Test Home Page
        properties_result_page: PropertiesResultPage = self._run_home_page_testing(search_criteria)

        # Test 2: Test Properties Result Page
        confirmation_page: ConfirmationPage = self._run_properties_result_page_testing(
            properties_result_page,
            filter_criteria)

        # Test 3: Test Booking Confirmation Page
        self._run_confirmation_page_testing(
            confirmation_page,
            filter_criteria)

        # Test 4: Test Payment and Reservation Page

        self.logger.info('***END OF PROPERTY BOOKING TESTING***\n')

    def _login(self) -> None:
        # Load cookies (if exists) for login session
        cookies_exist: bool = self._load_cookies()
        if cookies_exist:
            self.driver.refresh()
            login_success: bool = self.login_page.confirm_login()
            assert login_success, 'Login failed'
        else:
            raise Exception('Login has failed!')
            
    def _load_cookies(self) -> bool:
        try:
            cookies_helper.load_cookies(
                self.driver, 
                self.config.login_cookies_path,
                self.logger)
            return True
        except Exception as e:
            exception_msg = f'\nError loading cookies...\n Details: {e}'
            print(exception_msg)
            self.logger.error(exception_msg)
            return False

    def _run_home_page_testing(
            self,
            test_data: SearchCriteria) -> PropertiesResultPage:
        self.logger.info('Home page: selecting currency, destination, dates, and guest.')

        # Home page
        home_page = PageFactory.create_page(self.driver, HomePage)

        # Select currency
        home_page.select_currency(test_data.currency)
        selected_currency = home_page.confirm_current_currency()
        assert selected_currency == test_data.expected_currency, 'Currency mismatch'

        # Choose destination
        home_page.select_destination(test_data.destination)
        selected_destination = home_page.confirm_destination()
        assert selected_destination == test_data.expected_destination, 'Destination mismatch'

        # Select checkin and checkout dates
        home_page.add_checkin_and_checkout_dates(test_data.checkin_date, test_data.checkout_date)
        selected_dates = home_page.confirm_checkin_and_checkout_dates()
        assert selected_dates == (test_data.expected_checkin_date,test_data. expected_checkout_date), 'Check-in and check-out dates mismatch'

        # Add guests
        home_page.add_guests(
            adults=test_data.adult_count, 
            children=test_data.children_count, 
            infants=test_data.infant_count, 
            pets=test_data.pet_count)
        selected_guests = home_page.confirm_guests()
        assert selected_guests == test_data.expected_guests, 'Number and/or type of guest mismatch'

        # Search properties, and get result page object
        properties_result_page = home_page.search_and_get_result_page()
        return properties_result_page

    def _run_properties_result_page_testing(
            self, 
            properties_result_page: PropertiesResultPage,
            test_data: FilterCriteria) -> ConfirmationPage:
        self.logger.info('Properties rsult page: applying filters.')

        properties_result_page.apply_all_filters(
            type_of_place=test_data.type_of_place,
            min_price=test_data.min_price,
            max_price=test_data.max_price,
            bathrooms_count=test_data.bathrooms_count,
            property_type=test_data.property_type,
            amenity_options=test_data.amenity_options,
            booking_options=test_data.booking_options)
        confirmation_page = properties_result_page.choose_property_and_get_confirmation_page()
        return confirmation_page
    
    def _run_confirmation_page_testing(
        self,
        confirmation_page: ConfirmationPage,
        test_data: FilterCriteria) -> PaymentAndReservationPage:
        self.logger.info('Confirmation page: verifying property information.')

        # Switch to a new tab
        self.driver.switch_to.window(self.driver.window_handles[1])
        
        # Move this to page objects class
        # Close popups
        popups_handler.close_popup(
            self.driver,
            ConfirmationPageLocators.POPUP_CLOSE_BTN,
            self.logger)
        
        # Check price per night 
        price_per_night: float = confirmation_page.confirm_price_per_night()
        assert test_data.min_price <= price_per_night <= test_data.max_price, 'Price for a night stay mismatch'
        
        # Check selected amenities
        requested_amenities: Set[str, ...] = set(test_data.amenity_options)
        offerred_amenities: Set[str, ...] = set(confirmation_page.confirm_amenities())
        assert requested_amenities.issubset(offerred_amenities), 'Selected amenities mismatch'
        
        payment_and_reservation_page = confirmation_page.reserve_and_get_payment_and_reservation_page()
        return payment_and_reservation_page
   
    def _run_payment_and_reservation_page_testing(
        self,
        payment_and_reservation_page: PaymentAndReservationPage,
        payment_data: dict):
        self.logger.info('Payment page: making payment, and submitting booking request.')
        self._run_payment_form_testing(payment_and_reservation_page, payment_data)
        #self._run_reservation_testing()

    def _run_payment_form_testing(
        self,
        payment_and_reservation_page: PaymentAndReservationPage,
        payment_data: dict):
        payment_and_reservation_page.fill_up_payment_details(
            card_number=payment_data['card_number'],
            expiry_date=payment_data['expiry_date'],
            cvv=payment_data['cvv'],
            zip_code=payment_data['zip_code'])

    @mock.patch.object(
        PaymentAndReservationPage, 
        'confirm_and_pay', 
        return_value={ 'status': 'success' },
        autospec=True)
    def _run_reservation_testing(self, mock_confirm_and_pay):
        payment_and_reservation_page = PageFactory.create_page(
            self.driver,
            PaymentAndReservationPage)
        response = payment_and_reservation_page.confirm_and_pay()
        mock_confirm_and_pay.assert_called_once()
        assert response['status'] == 'success', 'Reservation failed'