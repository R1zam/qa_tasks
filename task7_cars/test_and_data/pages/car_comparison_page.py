from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.pages.base_form_page import BaseForm
from test_and_data.pages.car_form import CarForm


class ComparisonPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//h1[contains(@class,'compare-details-header')]"),
                                           'side_by_side_compare_page_unique_button')
        self.__name = 'ComparisonPage'
        self.__form = CarForm()
        super().__init__(self.__unique_element, self.__name)

    @property
    def form(self):
        return self.__form

    __first_car_engine = SimpleText(
        (By.XPATH, "(//td[contains(text(),'Engine')]/parent::tr/following-sibling::tr//p)[1]"), 'first_car_engine')
    __second_car_engine = SimpleText(
        (By.XPATH, "(//td[contains(text(),'Engine')]/parent::tr/following-sibling::tr//p)[2]"), 'second_car_engine')
    __first_car_transmission = SimpleText(
        (By.XPATH, "(//td[contains(text(),'Transmissions')]/parent::tr/following-sibling::tr//p)[1]"),
        'first_car_engine')
    __second_car_transmission = SimpleText(
        (By.XPATH, "//td[contains(text(),'Transmissions')]/parent::tr/following-sibling::tr//td[2]//p"),
        'first_car_engine')

    def get_first_car_options(self):
        engine = self.__first_car_engine.get_text()
        transmission = self.__first_car_transmission.get_text()
        return engine, transmission

    def get_second_car_options(self):
        engine = self.__second_car_engine.get_text()
        transmission = self.__second_car_transmission.get_text()
        return engine, transmission
