from selenium.webdriver.support.select import Select
from framework.elements.base_element import BaseElement
from random import randint, choice


class SelectElement(BaseElement):
    def __init__(self, by_locator, string_name):
        super().__init__(by_locator, string_name)

    def create_select_element(self):
        select_object = Select(self._find_element())
        return select_object

    def select_by_random_index(self):
        options = len(self.create_select_element().options) - 1
        n = randint(1, options)
        return self.create_select_element().select_by_index(n)

    def get_option(self):
        options = self.create_select_element().options[1:]
        option = choice(options).get_attribute('value')
        return option

    def select_by_value(self, value):
        self.create_select_element().select_by_value(value)

    def select_by_visible_text(self, text):
        self.create_select_element().select_by_visible_text(text)
