import pytest
from framework.driver_singltones.chrome_singleton import WebDriverChrome
from framework.driver_singltones.firefox_singleton import WebDriverFirefox
from framework.driver_singltones.base_abstract_creator import AbstractCreator


class WebDriverFactory(AbstractCreator):
    BROWSER_TYPES = {
        "chrome": WebDriverChrome(),
        "firefox": WebDriverFirefox()
    }

    def __init__(self, browser):
        super().__init__(browser)

    def choose_browser(self):
        self.driver = self.BROWSER_TYPES.get(self.browser,
                                             pytest.UsageError("browser_name should be chrome or firefox"))
        return self.driver
