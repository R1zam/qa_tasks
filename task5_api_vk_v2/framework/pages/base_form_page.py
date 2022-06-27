from abc import ABC
from framework.utils.wait_utils import WaitUtils
from conftest import logger

wait_utils = WaitUtils()


class BaseForm(ABC):

    def __init__(self, unique_element, page_name):
        self.__unique_element = unique_element
        self.__page_name = page_name

    @property
    def page_name(self):
        return self.__page_name

    @property
    def unique_element(self):
        return self.__unique_element

    def wait_until_loaded_and_check_if_displayed(self):
        logger.info(f"Waiting while page : {self.page_name} will open")
        wait_utils.wait_for_visibility(self.unique_element)
        logger.info(f"Checking if page : {self.page_name} is opened")
        return self.unique_element.is_displayed()
