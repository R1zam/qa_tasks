from conftest import logger


class DriverUtils():

    @staticmethod
    def get(driver, url):
        logger.info(f'Trying to open url : {url}')
        driver.get(url)

    @staticmethod
    def forward(driver):
        driver.forward()

    @staticmethod
    def back(driver):
        driver.back()

    @staticmethod
    def refresh(driver):
        driver.refresh()

    @staticmethod
    def set_size(driver, width, height):
        driver.set_window_size(width=width, height=height)

    @staticmethod
    def fullscreen_mode(driver):
        driver.fullscreen_window()

    @staticmethod
    def get_current_window(driver):
        return driver.current_window_handle

    @staticmethod
    def switch_window(driver, window):
        logger.info(f'Attempting to switch the window')
        driver.switch_to.window(window)

    @staticmethod
    def get_all_windows(driver):
        logger.info(f'Attempting to get all browser windows')
        return driver.window_handles

    @staticmethod
    def switch_window_number(driver, windows, window_number):
        logger.info(f'Attempting to switch the window')
        driver.switch_to.window(windows[window_number])

    @staticmethod
    def close_tab(driver):
        logger.info(f'Closing current tab')
        driver.close()
