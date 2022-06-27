from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.elements.button import Button
from framework.pages.base_form_page import BaseForm
from test_and_data.pages.car_form import CarForm


class MainPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'sds-home-search']"), 'main_page_unique_button')
        self.__name = 'MainPage'
        self.__form = CarForm()
        super().__init__(self.__unique_element, self.__name)

    @property
    def form(self):
        return self.__form

    __research_button = Button((By.XPATH, "//a[normalize-space()='Research & Reviews']"), 'research_button ')

    def click_on_research_button(self):
        self.__research_button.click()
