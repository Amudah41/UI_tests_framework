from task_3.framework.utils.Waits import Waits
from task_3.framework.utils.Loger import Loger


class BaseElement:
    def __init__(self, name, locator):
        self.name = name
        self.locator = locator

    def click(self):
        Loger().log(f"Click {self.name} element.")
        Waits.find_clickable_element(self.locator).click()

    def text(self):
        Loger().log(f"Wait for {self.name} element is displayed.")
        return Waits.find_element(self.locator).text

    def WaitForisDisplayed(self):
        Loger().log(f"Wait for {self.name} element is displayed.")
        return Waits.find_element(self.locator)

    def find_elements(self, elements_locator):
        Loger().log(f"Find elements of {self.name}")
        return Waits.find_elements(elements_locator)

    def click_and_write_text(self, text):
        Loger().log(f"Click {self.name} element.")
        element = Waits.find_clickable_element(self.locator)
        element.click()
        element.send_keys(text)
