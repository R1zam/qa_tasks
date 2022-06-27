from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.elements.button import Button
from framework.pages.base_form_page import BaseForm
from framework.utils.wait_utils import WaitUtils


class CarForm(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//a[@class='header-signin']"), 'car_form_page_unique_button')
        self.__name = 'CarFormPage'
        super().__init__(self.__unique_element, self.__name)

    __home_page_button = Button((By.XPATH, "//img[@alt='Cars.com Homepage']"), "home_page_button")
    __research_page_button = Button((By.XPATH, "//a[normalize-space()='Research & Reviews']"), "home_page_button")

    def go_on_main_page(self):
        WaitUtils.wait_for_visibility(self.__home_page_button)
        self.__home_page_button.click()

    def go_to_research_page(self):
        WaitUtils.wait_for_visibility(self.__research_page_button)
        self.__research_page_button.click()
