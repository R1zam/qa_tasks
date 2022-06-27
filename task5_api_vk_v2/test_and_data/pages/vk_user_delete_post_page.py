from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.pages.base_form_page import BaseForm
from framework.utils.wait_utils import WaitUtils
from test_and_data.pages.vk_user_page import VkUserFormPage


class VkUserDeletePostPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'page_avatar_wrap']"),
                                           'vk_user_page_unique_button')
        self.__name = 'Vk_User_Delete_POst_Page'
        super().__init__(self.__unique_element, self.__name)

    __form = VkUserFormPage()

    def check_post_deletion(self, deletion_time):
        WaitUtils.wait_until_closed(self.__form.post_field, deletion_time)
        return bool(self.__form.post_field.is_displayed())
