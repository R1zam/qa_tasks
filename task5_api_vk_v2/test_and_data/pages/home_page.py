from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.elements.button import Button
from framework.pages.base_form_page import BaseForm


class HomePage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'stories_feed_cont']"), 'home_page_unique_button')
        self.__name = 'Home_Page'
        super().__init__(self.__unique_element, self.__name)

    __my_page_button = Button((By.XPATH, "//span[contains(text(),'Моя страница')]"), 'my_page_unique_button')

    def go_on_my_page(self):
        self.__my_page_button.click()


