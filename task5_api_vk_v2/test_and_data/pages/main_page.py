from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.elements.button import Button
from framework.elements.text_field import TextField
from framework.pages.base_form_page import BaseForm
from framework.utils.wait_utils import WaitUtils

class MainPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@id='index_login']"), 'main_page_unique_button')
        self.__name = 'Main_Page'
        super().__init__(self.__unique_element, self.__name)

    __log_field = TextField((By.XPATH, "//input[@name='login']"), "log_field_text")
    __continue_button = Button((By.XPATH, "//div[contains(@class,'title')]"), "continue_button")
    __next_button = Button((By.XPATH,"//div[contains(@class,'Button__title')]"),"next_button")
    __pass_field = TextField((By.XPATH, "//input[@name = 'password']"), "pass_field_text")
    __enter_button = Button((By.XPATH, "//button[contains(@class, 'primary')]"), "enter_button")

    def vk_authorization(self, log, pass_):
        self.__enter_button.click()
        self.__log_field.send_text(log)
        self.__continue_button.click()
        WaitUtils.wait_for_visibility(self.__pass_field)
        self.__pass_field.send_text(pass_)
        self.__next_button.click()
