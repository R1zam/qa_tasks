from selenium import webdriver
from framework.driver_singltones.base_meta_singlton import MetaClassSingleton
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFirefox(metaclass=MetaClassSingleton):
    connection = None

    def get_driver(self):
        if self.connection is None:
            self.connection = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        return self.connection

    def driver_quit_and_set_connection_to_none(self):
        self.connection.quit()
        self.connection = None
