import os
import pickle
import logging
from typing import List, Dict, Optional, Union

from selenium.webdriver.remote.webdriver import WebDriver

DEFAULT_COOKIES_PATH = os.path.join('..', 'cookies', 'default_login_cookies.pkl')

def save_cookies(
    driver: WebDriver, 
    path: Optional[Union[str, os.PathLike]] = DEFAULT_COOKIES_PATH,
    logger: logging = None) -> None:
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Get and save cookies
        cookies: List[Dict] = driver.get_cookies()
        with open(path, 'wb') as file:
            pickle.dump(cookies, file)
    except PermissionError:
        exception_msg = f'Permission denied when trying to write cookies to {path}'
        if logger:
            logger.error(exception_msg)
        raise IOError(exception_msg)
    except Exception as e:
        exception_msg = f'Error saving cookies to {path}: {e}'
        if logger:
            logger.error(exception_msg)
        raise IOError(exception_msg)

def load_cookies(
    driver: WebDriver, 
    path: Optional[Union[str, os.PathLike]] = DEFAULT_COOKIES_PATH,
    logger: logging = None) -> None:
    try:
        # Check if file exists
        if not os.path.exists(path):
            raise FileNotFoundError(f'Cookies file not found at {path}') 
        # Load cookies
        with open(path, 'rb') as file:
            cookies: List[Dict] = pickle.load(file)
        # Add cookies to driver
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except Exception as add_cookie_error:
                print(f'Warning: Could not add cookie {cookie.get("name", "unnamed")}: {add_cookie_error}')
    except PermissionError:
        exception_msg = f'Permission denied when trying to read cookies from {path}'
        if logger:
            logger.error(exception_msg)
        raise IOError(exception_msg)
    except pickle.UnpicklingError:
        exception_msg = f'Invalid or corrupted cookies file at {path}'
        if logger:
            logger.error(exception_msg)
        raise ValueError(exception_msg)
    except Exception as e:
        exception_msg = f'Error loading cookies from {path}: {e}'
        if logger:
            logger.error(exception_msg)
        raise IOError(exception_msg)

def clear_cookies(
    path: Optional[Union[str, os.PathLike]] = DEFAULT_COOKIES_PATH,
    logger: logging = None) -> None:
    try:
        if os.path.exists(path):
            os.remove(path)
    except PermissionError:
        exception_msg = f'Permission denied when trying to remove cookies file at {path}'
        if logger:
            logger.error(exception_msg)
        raise IOError(exception_msg)
    except Exception as e:
        exception_msg = f'Error removing cookies file at {path}: {e}'
        if logger:
            logger.error(exception_msg)
        raise IOError(exception_msg)