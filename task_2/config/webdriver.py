from selenium import webdriver
from task_2.config._webdriver import SingletoneWebDriver


class WebDriver(webdriver.Chrome):

    driver = None
    is_closed = False

    def quit(self):
        webdriver.Chrome.quit(self)
        self.is_closed = True

    def __init__(self):
        if not self.driver or self.is_closed:
            self.driver = SingletoneWebDriver().get_driver
            self.is_closed = False
