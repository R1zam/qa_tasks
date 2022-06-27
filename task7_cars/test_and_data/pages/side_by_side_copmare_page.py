from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.elements.button import Button
from framework.elements.select_element import SelectElement
from framework.pages.base_form_page import BaseForm
from framework.utils.wait_utils import WaitUtils
from test_and_data.pages.car_form import CarForm
from framework.elements.link import Link


class SideBySideComparePage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//h2[normalize-space()='Start your own comparison']"),
                                           'side_by_side_compare_page_unique_button')
        self.__name = 'SideBySideComparePage'
        self.__form = CarForm()
        super().__init__(self.__unique_element, self.__name)

    @property
    def form(self):
        return self.__form

    __first_car_link = Link((By.XPATH, "//a[@phx-value-vehicle_index='vehicle_1']"), 'first_car_link")')
    __second_car_link = Link((By.XPATH, "//a[@phx-value-vehicle_index='vehicle_2']"), 'second_car_link")')
    __form_field = SimpleText((By.XPATH, "//div[@class = 'sds-modal__content']//h2"), "form_field")
    __make_option = SelectElement((By.XPATH, "//select[@id='vehicle_selection_make']"), "make_option")
    __model_option = SelectElement((By.XPATH, "//select[@id='vehicle_selection_model']"), "model_option")
    __year_option = SelectElement((By.XPATH, "//select[@id='vehicle_selection_year']"), "year_option")
    __trim_option = SelectElement((By.XPATH, "//select[@id='vehicle_selection_trim']"), "trim_option")
    __add_car_button = Button((By.XPATH, "//button[@type='submit']"), "add_car_button")
    __car_one_comparison_flag = SimpleText((By.XPATH, "//div[contains(@class,'card1 empty')]"), "car_one_flag")
    __car_two_comparison_flag = SimpleText((By.XPATH, "//div[contains(@class,'card1 empty')]"), "car_two_flag")
    __see_the_comparison_button = Button((By.XPATH, "//button[normalize-space()='See the comparison']"),
                                         "see_the_comparison_button")

    def click_on_first_car_row(self):
        self.__first_car_link.click()

    def click_on_second_car_row(self):
        WaitUtils.wait_for_click(self.__second_car_link)
        self.__second_car_link.click()

    def add_car_to_compare(self, make, model, year, trim):
        WaitUtils.wait_for_visibility(self.__form_field)
        self.__make_option.select_by_value(make)
        WaitUtils.wait_for_click(self.__model_option)
        self.__model_option.select_by_value(model)
        WaitUtils.wait_for_click(self.__year_option)
        self.__year_option.select_by_value(year)
        WaitUtils.wait_for_click(self.__trim_option)
        self.__trim_option.select_by_visible_text(trim)
        WaitUtils.wait_for_click(self.__add_car_button)
        self.__add_car_button.click()

    def is_car_one_chosen(self, time):
        WaitUtils.wait_until_closed(self.__car_one_comparison_flag, time)
        return not bool(self.__car_one_comparison_flag._find_elements())

    def is_car_two_chosen(self, time):
        WaitUtils.wait_until_closed(self.__car_two_comparison_flag, time)
        return not bool(self.__car_two_comparison_flag._find_elements())

    def go_to_comparison_page(self):
        WaitUtils.wait_for_click(self.__see_the_comparison_button)
        self.__see_the_comparison_button.click()
