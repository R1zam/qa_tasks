from PIL import Image
from urllib.request import urlopen
import numpy as np
from selenium.webdriver.common.by import By
from framework.pages.base_form_page import BaseForm
from framework.elements.simple_text import SimpleText
from framework.elements.button import Button
from framework.utils.wait_utils import WaitUtils
from test_and_data.pages.vk_user_page import VkUserFormPage


class VkUserEditPostPage(BaseForm):
    def __init__(self):
        self.__unique_element = SimpleText((By.XPATH, "//div[@class = 'page_avatar_wrap']"),
                                           'vk_user_page_unique_button')
        self.__name = 'Vk_User_Edit_Post_Page'
        super().__init__(self.__unique_element, self.__name)

    __form = VkUserFormPage()
    __text_field = SimpleText((By.XPATH, f"(//div[contains(@class , 'post_text')])[1]"), "text_field")
    __image_wall_field = Button((By.XPATH, f"//div[contains(@id,'wpt{__form.USER_ID}')]//a[@aria-label='фотография']"),
                                "image_wall_button")
    __image_link_field = Button((By.XPATH, f"//div[@id='pv_photo']//img"),
                                "image_link_button")
    __close_button = Button((By.XPATH, f"//div[@class='pv_close_btn']"),
                            "close_button")

    def get_text_from_wall(self):
        return self.__text_field.get_text()

    def get_image_and_calc_pixel_sum(self):
        self.__image_wall_field.click()
        WaitUtils.wait_for_visibility(self.__image_link_field)
        url = self.__image_link_field._find_element().get_attribute("src")
        img = Image.open(urlopen(url))
        self.__close_button.click()
        return sum(np.array(img).flatten())
