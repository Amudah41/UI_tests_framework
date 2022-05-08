from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from task_3.framework.config.config_data import TimeOut_default
from task_3.framework.utils.Browser import Browser


class Waits:
    @staticmethod
    def find_element(locator, time=TimeOut_default):
        return WebDriverWait(Browser.get_driver(), time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    @staticmethod
    def find_clickable_element(locator, time=TimeOut_default):
        return WebDriverWait(Browser.get_driver(), time).until(
            EC.element_to_be_clickable(locator),
            message=f"Can't find element by locator {locator}",
        )

    @staticmethod
    def find_visible_element(locator, time=TimeOut_default):
        return WebDriverWait(Browser.get_driver(), time).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find visible element by locator {locator}",
        )

    @staticmethod
    def find_elements(locator, time=TimeOut_default):
        return WebDriverWait(Browser.get_driver(), time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
