from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from task_2.tests.test_data import URL
from task_2.config.config_data import TimeOut_default


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL

    def find_element(self, locator, time=TimeOut_default):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_visible_element(self, locator, time=TimeOut_default):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find visible element by locator {locator}",
        )

    def find_elements(self, locator, time=TimeOut_default):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def move_to_element(self, element):
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
