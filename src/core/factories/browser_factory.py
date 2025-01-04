from typing import Literal, Dict, Callable

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver

class BrowserFactory:
    @staticmethod
    def get_driver(
        browser_name: Literal['chrome', 'firefox'] = 'chrome', 
        headless: bool = False, 
        incognito: bool = False):
        drivers: Dict[str, Callable[[bool, bool], WebDriver]] = {
            'chrome': BrowserFactory._get_chrome_driver,
            'firefox': BrowserFactory._get_firefox_driver
        }

        browser_name = browser_name.lower()
        if browser_name not in drivers:
            raise ValueError(f'{browser_name} is not supported. Supported browsers are: {list(drivers.keys())}')
        
        return drivers[browser_name](headless, incognito)
    
    @staticmethod
    def _get_chrome_driver(headless: bool, incognito: bool) -> ChromeWebDriver:
        chrome_options = ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
        if incognito:
            chrome_options.add_argument('--incognito')
        chrome_options.add_experimental_option('detach', True)
        return webdriver.Chrome(options=chrome_options)

    @staticmethod
    def _get_firefox_driver(headless: bool, incognito: bool) -> FirefoxWebDriver:
        firefox_options = FirefoxOptions()
        if headless:
            firefox_options.add_argument('-headless') 
        if incognito:
            firefox_options.add_argument('-private')
        return webdriver.Firefox(options=firefox_options)

    @staticmethod
    def quit_driver(driver: WebDriver) -> None:
        if driver:
            driver.quit()