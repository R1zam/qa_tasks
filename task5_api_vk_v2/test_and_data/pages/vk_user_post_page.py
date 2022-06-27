from selenium.webdriver.common.by import By
from framework.pages.base_form_page import BaseForm
from framework.elements.simple_text import SimpleText
from framework.utils.other_utils.test_data import TestData
from test_and_data.pages.vk_user_page import VkUserFormPage
import re

test_data = TestData("test_data.json")


class VkUserPostPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'page_avatar_wrap']"),
                                           'vk_user_page_unique_button')
        self.__name = 'Vk_User_Post_Page'
        super().__init__(self.__unique_element, self.__name)

    __form = VkUserFormPage()

    __post_text_field = SimpleText((By.XPATH, f"{__form.post_prefix}//div[contains(@class, 'zoom_text')]"),
                                   'post_text_field')
    __post_author_field = SimpleText((By.XPATH, f"{__form.post_prefix}//h5//a"),
                                     'post_author_field')

    def check_post_data(self):
        self.__form.wait_for_post_prefix()
        __post_text = self.__post_text_field.get_text()
        post_author_dirty = self.__post_author_field._find_element().get_attribute("href")
        post_author_id = int(re.search(r'[0-9]+', post_author_dirty).group())
        return post_author_id, __post_text
