from framework.elements.base_element import BaseElement


class Link(BaseElement):
    def __init__(self, by_locator, string_name):
        super().__init__(by_locator, string_name)
