from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.pages.base_form_page import BaseForm
from framework.utils.wait_utils import WaitUtils
from framework.utils.other_utils.test_data import TestData

test_data = TestData("test_data.json")


class VkUserFormPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'page_avatar_wrap']"),
                                           'vk_user_page_unique_button')
        self.__name = 'Vk_User_Page'
        super().__init__(self.__unique_element, self.__name)

    USER_ID = test_data.get_data("user_id_param1")[1]
    __post_prefix = f"(//div[contains(@id , 'post{USER_ID}')])[1]"
    __post_field = SimpleText((By.XPATH, __post_prefix),
                              'post_field_info')

    @property
    def post_prefix(self):
        return self.__post_prefix

    @property
    def post_field(self):
        return self.__post_field

    def wait_for_post_prefix(self):
        WaitUtils.wait_for_visibility(self.__post_field)
