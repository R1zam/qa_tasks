from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from framework.driver_singltones.base_meta_singlton import MetaClassSingleton


class WebDriverChrome(metaclass=MetaClassSingleton):
    connection = None
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    def get_driver(self):
        if self.connection is None:
            self.connection = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=self.chrome_options)
        return self.connection

    def driver_quit_and_set_connection_to_none(self):
        self.connection.quit()
        self.connection = None
