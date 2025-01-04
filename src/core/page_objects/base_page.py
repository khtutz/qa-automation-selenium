from typing import Callable, Tuple, Union, Any, Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    TimeoutException, 
    NoSuchElementException, 
    StaleElementReferenceException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CoreBasePage:
    @classmethod
    def wait_and_perform_action(
        cls,
        driver: WebDriver,
        locator: Tuple[Union[By, str], str], 
        *condition_args,
        action: Optional[Callable[[WebElement], Any]] = None,
        condition: Callable[[Tuple[Union[By, str], str]], WebElement] = EC.presence_of_element_located,
        action_count: int = 1,
        clear_input_element = False,
        timeout: float = 20,
        logger = None
    ) -> Optional[WebElement]:
        try:
            WebDriverWait(driver, timeout).until(
                condition(locator, *condition_args))
            element = driver.find_element(*locator)

            if clear_input_element:
                element.send_keys(Keys.COMMAND + 'a')
                element.send_keys(Keys.BACKSPACE)

            if action:
                for _ in range(action_count):
                    action(element)
                
            return element
        except TimeoutException as e:
            if logger:
                logger.error(f'Timeout: Condition not met for locator {locator} within {timeout}s. Details: {e}')
            raise
        except NoSuchElementException as e:
            if logger:
                logger.error(f'Error: Element with locator {locator} was not found in the DOM. Details: {e}')
            raise
        except Exception as e:
            if logger:
                logger.error(f'Error has occurred for element: {locator}. Details: {e}')
            raise

    @classmethod
    def perform_action(
        cls,
        driver: WebDriver,
        locator: Tuple[Union[By, str], str],
        action: Optional[Callable[[WebElement], Any]] = None,
        action_count: int = 1,
        clear_input_element = False,
        logger = None) -> Optional[WebElement]:
        try:
            element = driver.find_element(*locator)

            if clear_input_element:
                element.send_keys(Keys.COMMAND + 'a')
                element.send_keys(Keys.BACKSPACE)

            if action:
                for _ in range(action_count):
                    action(element)

            return element
        except NoSuchElementException as e:
            exception_msg = f'Error: Element with locator {locator} was not found. Details: {e}'
            if logger:
                logger.error(exception_msg)
            raise
        except StaleElementReferenceException as e:
            exception_msg = f'Error: Element with locator {locator} is no longer attached to the DOM. Details: {e}'
            if logger:
                logger.error(exception_msg)
            raise

    @classmethod
    def wait_for_element_until_not_attached_to_DOM(
        cls,
        driver: WebDriver,
        locator: Tuple[Union[By, str], str],
        timeout: float = 20,
        logger = None) -> None:
        try:
            WebDriverWait(driver, timeout).until(
                EC.staleness_of(driver.find_element(*locator)))     
        except TimeoutException as e:
            if logger:
                logger.error(f'Timeout: Element with locator {locator} did not disappear within {timeout}s. Details: {e}')
            raise
        except Exception as e:
            if logger:
                logger.error(f'Error has occurred for element: {locator}. Details: {e}')
            raise

    @classmethod
    def wait_for_invisibility_of_element(
        cls,
        driver: WebDriver,
        locator: Tuple[Union[By, str], str],
        timeout: float = 20,
        logger = None) -> None:
        try:
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element(locator))     
        except TimeoutException as e:
            if logger:
                logger.error(f'Timeout: Element with locator {locator} did not disappear within {timeout}s. Details: {e}')
            raise
        except Exception as e:
            if logger:
                logger.error(f'Error has occurred for element: {locator}. Details: {e}')
            raise