from selenium.webdriver.common.by import By
from framework.elements.simple_text import SimpleText
from framework.pages.base_form_page import BaseForm


class VkUserLikesPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'page_avatar_wrap']"),
                                           'vk_user_page_unique_button')
        self.__name = 'Vk_User_Likes_Page'
        super().__init__(self.__unique_element, self.__name)

    like_button = SimpleText((By.XPATH,
                              f"(//div[contains(@class , 'like_wall')])[1]//div[@class='PostButtonReactions__icon ']//*[name()='svg']"),
                             'like_button')

    def click_like_on_post(self):
        self.like_button.click()
