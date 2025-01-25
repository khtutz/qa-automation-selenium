from typing import  Callable, Tuple, List, Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    NoSuchElementException, 
    WebDriverException, 
    StaleElementReferenceException
)

from src.travel_airbnb.utils.config_reader import ConfigReader
from src.core.page_objects.base_page import CoreBasePage
from src.travel_airbnb.utils.logging_helper import get_logger

class BasePage(CoreBasePage):
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.config = ConfigReader()
        self.logger = get_logger(self.__class__.__name__)

    def wait_for_page_load(self):
        # Placeholder method to be overridden by specific page classes
        raise NotImplementedError("Subclasses must implement wait_for_page_load")
    
    def wait_and_find_element(
            self, 
            locator: Tuple[Union[By, str], str], 
            condition: Callable[[Tuple[Union[By, str], str]], WebElement] = EC.presence_of_element_located, 
            *condition_args,
            timeout: float = 20) -> WebElement:
        return super().wait_and_perform_action(
            self.driver,
            locator,
            *condition_args,
            action=None,
            condition=condition,
            action_count=1,
            clear_input_element=False,
            timeout=timeout,
            logger=self.logger)

    def wait_for_element_and_click(
            self, 
            locator: Tuple[Union[By, str], str], 
            condition: Callable[[Tuple[Union[By, str], str]], WebElement] = EC.presence_of_element_located, 
            *condition_args,
            action_count: int = 1,
            timeout: float = 20) -> WebElement:
        return super().wait_and_perform_action(
            self.driver,
            locator,
            *condition_args,
            action=lambda element: element.click(),
            condition=condition,
            action_count=action_count,
            clear_input_element=False,
            timeout=timeout,
            logger=self.logger)
        
    def wait_for_element_and_send_keys(
            self, 
            locator: Tuple[Union[By, str], str],
            value: str,
            condition: Callable[[Tuple[Union[By, str], str]], WebElement] = EC.presence_of_element_located, 
            *condition_args,
            clear_input_element: bool = False,
            timeout: float = 20) -> WebElement:
        return super().wait_and_perform_action(
            self.driver,
            locator, 
            *condition_args,
            action=lambda element: element.send_keys(value), 
            condition=condition,
            action_count=1,
            clear_input_element=clear_input_element,
            timeout=timeout,
            logger=self.logger)

    def wait_for_element_to_disappear(
            self,
            locator: Tuple[Union[By, str], str],
            timeout: float = 20) -> None:
        return super().wait_for_element_until_not_attached_to_DOM(
            self.driver,
            locator,
            timeout=timeout,
            logger=self.logger)

    def find_element(self, locator: Tuple[Union[By, str], str]) -> None:
        return super().perform_action(
            self.driver,
            locator,
            action_count=1,
            clear_input_element=False,
            action=None,
            logger=self.logger)

    def find_element_and_click(
            self, 
            locator: Tuple[Union[By, str], str],
            action_count: int = 1) -> None:
        return super().perform_action(
            self.driver,
            locator,
            action_count=action_count,
            clear_input_element=False,
            action=lambda element: element.click(),
            logger=self.logger)

    def find_element_and_send_keys(
            self, 
            locator: Tuple[Union[By, str], str],
            value: str,
            clear_input_element=False) -> None:
        return super().perform_action(
            self.driver,
            locator,
            action=lambda element: element.send_keys(value),
            action_count=1,
            clear_input_element=clear_input_element,
            logger=self.logger)
    
    def find_element_and_get_text(self, locator: Tuple[Union[By, str], str]) -> str:
        return super().perform_action(
            self.driver,
            locator,
            action_count=1,
            clear_input_element=False,
            action=None,
            logger=self.logger).text
    
    def find_element_and_get_attribute(self, locator: Tuple[Union[By, str], str], name: str) -> str:
        attribute = super().perform_action(
            self.driver,
            locator,
            action_count=1,
            clear_input_element=False,
            action=None,
            logger=self.logger).get_attribute(name)
        return attribute if attribute else ''

    def find_elements(self, locator: Tuple[Union[By, str], str]) -> List[WebElement]:
        try:
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            error_msg = f'Error: Elements with locator {locator} was not found.'
            self.logger.error(error_msg)
            raise
        except StaleElementReferenceException:
            error_msg = f'Error: Elements with locator {locator} is no longer attached to the DOM.'
            self.logger.error(error_msg)
            raise
    
    def find_elements_and_click_nth_element(
        self, 
        locator: Tuple[Union[By, str], str],
        n: int) -> None:
        try:
            self.driver.find_elements(*locator)[n].click()
        except NoSuchElementException:
            error_msg = f'Error: Elements with locator {locator} was not found.'
            self.logger.error(error_msg)
            raise
        except StaleElementReferenceException:
            error_msg = f'Error: Elements with locator {locator} is no longer attached to the DOM.'
            self.logger.error(error_msg)
            raise

    def is_element_present(self, locator: Tuple[Union[By, str], str]) -> bool:
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def scroll_to_element(self, locator: Tuple[Union[By, str], str]) -> None:
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except NoSuchElementException:
            error_msg = f'Error: Element with locator {locator} was not found.'
            self.logger.error(error_msg)
            raise
        except WebDriverException as e:
            error_msg = f'Error scrolling to element with locator {locator}. Details: {e}'
            self.logger.error(error_msg)
            raise

    def is_user_logged_in(
            self, 
            locator: Tuple[Union[By, str], str],
            condition: Callable[[Tuple[Union[By, str], str]], WebElement] = EC.presence_of_element_located) -> bool:
        element = self.wait_and_find_element(locator, condition)
        return element.is_displayed()
        