from abc import ABC, abstractmethod


class AbstractCreator(ABC):
    def __init__(self, browser):
        self.browser = browser

    @abstractmethod
    def choose_browser(self):
        """Method to choose browser needed"""
