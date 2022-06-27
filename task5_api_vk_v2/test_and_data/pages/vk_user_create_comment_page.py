import re
from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.pages.base_form_page import BaseForm
from framework.utils.wait_utils import WaitUtils
from test_and_data.pages.vk_user_page import VkUserFormPage


class VkUserCreateCommentPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'page_avatar_wrap']"),
                                           'vk_user_page_unique_button')
        self.__name = 'Vk_User_Create_Comment_Page'
        super().__init__(self.__unique_element, self.__name)

    __form = VkUserFormPage()
    __show_comment_field = SimpleText(
        (By.XPATH, f"//span[@class='js-replies_next_label']"),
        'show_comment_field')
    __comment_text_field = SimpleText(
        (By.XPATH, f"{__form.post_prefix}//div[@class = 'reply_text']//div[@class = 'wall_reply_text']"),
        'comment_text_field')
    __author_field = SimpleText((By.XPATH, f"{__form.post_prefix}//div[@class = 'reply_author']//a"),
                                'author_field')

    def wait_for_post_prefix(self):
        WaitUtils.wait_for_visibility(self.__form.post_field)

    def check_comment_data(self):
        self.wait_for_post_prefix()
        WaitUtils.wait_for_visibility(self.__show_comment_field)
        self.__show_comment_field.click()
        WaitUtils.wait_for_visibility(self.__comment_text_field)
        comment_text = self.__comment_text_field.get_text()
        author_name_dirty = self.__author_field._find_element().get_attribute("href")
        author_name = int(re.search(r'[0-9]+', author_name_dirty).group())
        return author_name, comment_text
