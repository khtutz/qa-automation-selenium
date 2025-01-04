from selenium.webdriver.common.by import By
from typing import Tuple, Union

class CoreBaseLocators:
    @staticmethod
    def locator(
        by: Union[By, str], 
        value: str
    ) -> Tuple[Union[By, str], str]:
        return (by, value)
    
    @classmethod
    def css(cls, value: str) -> Tuple[Union[By, str], str]:
        return cls.locator(By.CSS_SELECTOR, value)
    
    @classmethod
    def xpath(cls, value: str) -> Tuple[Union[By, str], str]:
        return cls.locator(By.XPATH, value)
    
    @classmethod
    def id(cls, value: str) -> Tuple[Union[By, str], str]:
        return cls.locator(By.ID, value)
    
    @classmethod
    def class_name(cls, value: str) -> Tuple[Union[By, str], str]:
        return cls.locator(By.CLASS_NAME, value)
    
    @classmethod
    def data_testid(cls, value: str) -> Tuple[Union[By, str], str]:
        return cls.locator(By.CSS_SELECTOR, f'[data-testid="{value}"]')
