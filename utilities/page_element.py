from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageElement:

    def __init__(self, driver: WebDriver, locator: Tuple[str, str]):
        self.driver = driver
        self.locator = locator

    def _get_el(self) -> WebElement:
        return self.driver.find_element(*self.locator)

    def click(self) -> None:
        self._get_el().click()

    def send_keys(self, value: str) -> None:
        """
        Send 'value' to given element.

        :param value: value to send to the given element.
        """
        self._get_el().send_keys(value)
