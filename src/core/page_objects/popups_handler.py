import logging
from typing import Tuple, Union, Optional

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def close_popup(
        driver: WebDriver,
        locator: Tuple[Union[By, str], str], 
        logger: Optional[logging.Logger] = None,
        timeout: float = 25.0,
        silent: bool = False) -> bool:
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator))
        element.click()
        return True
    except NoSuchElementException as e:
        error_msg = f'Warning: Element with locator {locator} was not found in the DOM.'
        _handle_error(error_msg, logger, silent, is_warning=True)
        return False
    except WebDriverException as e:
        error_msg = f'Error closing popup for element: {locator}. Details: {str(e)}'
        _handle_error(error_msg, logger, silent, is_warning=False)
        return False
    
def _handle_error(
        error_msg: str, 
        logger: Optional[logging.Logger] = None, 
        silent: bool = False, 
        is_warning: bool = False) -> None:
    if not silent:
        print(error_msg)
    if logger:
        if is_warning:
            logger.warning(error_msg)
        else:
            logger.error(error_msg)
