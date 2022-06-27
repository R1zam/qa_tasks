from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.utils.config_utils import Config
from framework.driver_singltones.webdriver_factory import WebDriverFactory

config_data = Config("config_data.json")
timer = config_data.get_data('waiting_timer')


class WaitUtils():

    @staticmethod
    def wait_and_click(element):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer).until(
            EC.element_to_be_clickable(element.by_locator)).click()

    @staticmethod
    def wait_for_alert():
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer).until(
            EC.alert_is_present())

    @staticmethod
    def wait_for_presence(element):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer).until(
            EC.presence_of_element_located(element.by_locator))

    @staticmethod
    def wait_for_visibility(element):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer).until(
            EC.visibility_of_element_located(element.by_locator))

    @staticmethod
    def wait_for_text(element, text):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer).until(
            EC.text_to_be_present_in_element(element.by_locator, text))

    @staticmethod
    def wait_for_click(element):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer).until(
            EC.element_to_be_clickable(element.by_locator))

    @staticmethod
    def wait_for_staleness(element):
        return WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(),
                             timer).until(EC.staleness_of(element._find_element()))

    @staticmethod
    def wait_for_number_of_windows_needed(number):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer).until(
            EC.number_of_windows_to_be(number))

    @staticmethod
    def wait_for_attribute_value(element, attribute, text):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), timer,
                      0.05).until(
            EC.text_to_be_present_in_element_attribute(element.by_locator, attribute, text))

    @staticmethod
    def wait_until_closed(element, time):
        WebDriverWait(WebDriverFactory(config_data.get_data("browser")).choose_browser().get_driver(), time).until_not(
            EC.visibility_of_element_located(element.by_locator))
