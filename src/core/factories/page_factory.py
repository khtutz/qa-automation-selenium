from typing import Type, TypeVar
from selenium import webdriver

T = TypeVar('T')

class PageFactory:
    @staticmethod
    def create_page(driver: webdriver, page_class: Type[T]) -> T:
        page = page_class(driver)
        page.wait_for_page_load()
        return page