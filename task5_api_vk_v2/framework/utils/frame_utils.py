from selenium.webdriver.common.by import By
from conftest import logger


class FrameUtils:

    @staticmethod
    def switch_to_frame(driver, frame_id):
        logger.info("Switching to a new frame")
        driver.switch_to.frame(frame_id)

    @staticmethod
    def switch_to_frame_by_tag(driver):
        logger.info("Switching to a new frame")
        iframe = driver.find_element(By.TAG_NAME, 'iframe')
        driver.switch_to.frame(iframe)

    @staticmethod
    def escape_frame(driver):
        logger.info("Escaping from frame")
        driver.switch_to.default_content()
