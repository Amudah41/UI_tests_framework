from selenium.common.exceptions import TimeoutException
from task_3.framework.utils.Waits import Waits
from task_3.framework.utils.Loger import Loger
from task_3.framework.utils.Browser import Browser


class BaseForm:
    def __init__(self, name, locator):
        self.name = name
        self.locator = locator

    def is_loaded(self):
        try:
            Waits.find_element(self.locator)
            Loger().log(f"Page {self.name} is loaded.")
            return True
        except TimeoutException:
            return False

    @staticmethod
    def scroll_page_down_ot_element(element):
        Browser.scroll_page_down_until_element_not_visible(element.locator)

    @staticmethod
    def scroll_page_up():
        Browser.scroll_page_up()
