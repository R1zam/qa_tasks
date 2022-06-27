import pytest
from framework.utils.config_utils import Config
from framework.utils.logger_utils import Logger
from framework.driver_singltones.webdriver_factory import WebDriverFactory

logger = Logger()
config_data = Config("config_data.json")


@pytest.fixture(scope='function')
def driver():
    driver = WebDriverFactory.initialize_driver()
    driver.get(config_data.get_data('main_page_link'))
    yield driver
    WebDriverFactory(config_data.get_data("browser")).choose_browser().driver_quit_and_set_connection_to_none()
