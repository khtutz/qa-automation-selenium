import pytest
import time
from typing import Generator
from logging import Logger
from selenium.webdriver.remote.webdriver import WebDriver

from src.core.factories.browser_factory import BrowserFactory
from src.travel_airbnb.utils.logging_helper import get_logger
from src.travel_airbnb.utils.config_reader import ConfigReader

def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        '--browser_name', 
        action='store', 
        default='chrome')
    parser.addoption(
        '--headless', 
        action='store_true', 
        default=False,
        help='Run tests in headless mode')
    parser.addoption(
        '--env',
        action='store',
        default='development',
        help='Environment to run tests against (development/staging/production)')

@pytest.fixture(scope='session')
def config() -> ConfigReader:
    return ConfigReader()

@pytest.fixture(scope='class')
def setup(
    request: pytest.FixtureRequest,
    config: ConfigReader) -> Generator[None, None, None]:
    # Capture browser name from CLI
    browser_name = request.config.getoption('browser_name')
    headless = request.config.getoption('headless')

    # BrowserFactory to get the driver
    driver: WebDriver = BrowserFactory.get_driver(
        browser_name=browser_name,
        headless=headless,
        incognito=False)

    driver.get(config.base_url)
    driver.implicitly_wait(config.implicit_wait)

    # Make both driver and config available to test classes
    request.cls.driver = driver
    request.cls.config = config

    yield

    time.sleep(4)
    BrowserFactory.quit_driver(driver)

@pytest.fixture(scope='class')
def logger(request: pytest.FixtureRequest) -> None:
    # Test class/module name for the logger
    logger: Logger = get_logger(request.node.name)  
    request.cls.logger = logger