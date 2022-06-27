from conftest import logger
from selenium.common.exceptions import NoAlertPresentException


class AlertUtils:

    @staticmethod
    def alert_switch_and_click(driver):
        logger.info(f"Attempting to accept present alert")
        driver.switch_to.alert.accept()

    @staticmethod
    def alert_dismiss(driver):
        logger.info(f"Attempting to decline present alert")
        driver.switch_to.alert.dismiss()

    @staticmethod
    def alert_text(driver):
        logger.info(f"Attempting to get text from present alert")
        return driver.switch_to.alert.text

    @staticmethod
    def send_text_to_alert(driver, text):
        logger.info(f"Attempting to send message {text} to present alert")
        driver.switch_to.alert.send_keys(text)

    @staticmethod
    def is_present_alert(driver):
        logger.info("Checking if Alert is present")
        try:
            driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True
