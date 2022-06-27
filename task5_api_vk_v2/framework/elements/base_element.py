from abc import ABC
from conftest import logger
from framework.utils.config_utils import Config
from framework.driver_singltones.webdriver_factory import WebDriverFactory

config_data = Config("config_data.json")


class BaseElement(ABC):

    def __init__(self, by_locator, string_name):
        self.__by_locator = by_locator
        self.__name = string_name

    @property
    def by_locator(self):
        return self.__by_locator

    @property
    def name(self):
        return self.__name

    def click(self):
        logger.info(f"Clicking on {self.__class__.__name__} : {self.__name}")
        self._find_element().click()

    def get_text(self):
        logger.info(f"Trying to get text from {self.__class__.__name__} : {self.__name}")
        return self._find_element().text

    def is_displayed(self):
        return self._find_element().is_displayed()

    def _find_element(self):
        element = WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver().find_element(
            *self.by_locator)
        return element

    def _find_elements(self):
        elements = WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver().find_elements(
            *self.by_locator)
        return elements
