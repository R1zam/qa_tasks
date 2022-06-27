from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.elements.text_field import TextField
from framework.elements.link import Link
from framework.pages.base_form_page import BaseForm
from test_and_data.pages.car_form import CarForm
from selenium.common.exceptions import NoSuchElementException


class TrimComparisonPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText(
            (By.XPATH, "//p[contains(text(),'Our comparison will help you prioritize the trims ')]"),
            'trim_comparison_page_unique_button')
        self.__name = 'TrimComparisonPage'
        self.__form = CarForm()
        super().__init__(self.__unique_element, self.__name)

    @property
    def form(self):
        return self.__form

    __first_model_button = Link((By.XPATH, "(//button[contains(@id,'trigger1')])[1]"), "trim_list_link")
    __engine_field = TextField((By.XPATH,
                                "(//div[contains(@id,'research-compare')]//th[contains(text(),'Engine')]/parent::tr/following-sibling::tr/td)[1]"),
                               'engine_field')
    __transmission_field = TextField((By.XPATH,
                                      "(//div[contains(@id,'research-compare')]//th[contains(text(),'Transmission')]/parent::tr/following-sibling::tr/td)[1]"),
                                     "transmission_field")
    __trim_style = TextField((By.XPATH,
                              "(//div[contains(@id,'research-compare')]//th[contains(text(),'Style')]/parent::tr/following-sibling::tr/td)[1]"),
                             "trim_comparison_field")

    def expand_model_info(self):
        try:
            self.__first_model_button.click()
        except NoSuchElementException:
            pass

    def get_some_characteristics(self):
        try:
            trim = self.__trim_style.get_text()
            engine = self.__engine_field.get_text()
            transmission = self.__transmission_field.get_text()
            return trim, engine, transmission
        except NoSuchElementException:
            return None, None, None
