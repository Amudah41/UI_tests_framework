from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from task_2.config.config_data import WindowSize_LEN, WindowSize_HIGH


class SingletoneWebDriver:
    @property
    def get_driver(self):
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s)
        self.driver.set_window_size(WindowSize_LEN, WindowSize_HIGH)
        return self.driver
