from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.elements.button import Button
from framework.pages.base_form_page import BaseForm
from test_and_data.pages.car_form import CarForm
from framework.elements.select_element import SelectElement


class ResearchPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//h2[text() = 'Research cars']"), 'research_page_unique_button')
        self.__name = 'ResearchPage'
        self.__form = CarForm()
        super().__init__(self.__unique_element, self.__name)

    @property
    def form(self):
        return self.__form

    __car_make = SelectElement((By.XPATH, "//select[@id='make-select']"), "car_make_select")
    __model_select = SelectElement((By.XPATH, "//select[@id='model-select']"), "model_select")
    __year_select = SelectElement((By.XPATH, "//select[@id='year-select']"), "year_select")
    __research_button = Button((By.XPATH, "//button[contains(@class,'sds-button')]"), "research_button")
    __side_by_side_compare_button = Button((By.XPATH, "//a[normalize-space()='Compare models']"),
                                           "side_by_side_compare_button")

    def go_to_side_comparing_page(self):
        self.__side_by_side_compare_button.click()

    def get_make(self):
        return self.__car_make.get_option()

    def get_model(self):
        return self.__model_select.get_option()

    def get_year(self):
        return self.__year_select.get_option()

    def car_selection_and_store_data(self):
        make = self.get_make()
        self.__car_make.select_by_value(make)
        model = self.get_model()
        self.__model_select.select_by_value(model)
        year = self.get_year()
        self.__year_select.select_by_value(year)
        return make, model, year

    def click_on_research_button(self):
        self.__research_button.click()
