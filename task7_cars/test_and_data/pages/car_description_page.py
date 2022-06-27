from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.pages.base_form_page import BaseForm
from test_and_data.pages.car_form import CarForm
from framework.elements.link import Link


class CarDescriptionPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//h1[contains(@class,'sds-heading')]"),
                                           'car_description_page_unique_button')
        self.__name = 'CarDescriptionPage'
        self.__form = CarForm()
        super().__init__(self.__unique_element, self.__name)

    @property
    def form(self):
        return self.__form

    __trim_comparison_link = Link((By.XPATH, "//a[contains(normalize-space(),'trim comparison')]"),
                                  "trim_comparison_link")

    def go_to_trim_comparison(self):
        self.__trim_comparison_link.click()
