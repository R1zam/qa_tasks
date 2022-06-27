from framework.elements.base_element import BaseElement


class TextField(BaseElement):
    def __init__(self, by_locator, string_name):
        super().__init__(by_locator, string_name)

    def send_text(self, text):
        self._find_element().send_keys(text)

    def clear_input(self):
        self._find_element().clear()
