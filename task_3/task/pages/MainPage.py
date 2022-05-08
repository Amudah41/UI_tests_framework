from task_3.framework.pages.BaseForm import BaseForm
from selenium.webdriver.common.by import By
from task_3.task.elements.Button import Button


class MainPage(BaseForm):

    LOCATOR_MAIN_PAGE_UNIQUE_ELEMENT = (
        By.XPATH,
        "//div[@id='app']//div[@class='category-cards']",
    )

    LOCATOR_ALERTS_FRAME_AND_WINDOWS_BUTTON = (
        By.XPATH,
        "//div[@class='category-cards']/div[3]",
    )

    LOCATOR_ELEMENTS_BUTTON = (
        By.XPATH,
        "//div[@class='category-cards']/div[1]",
    )

    def __init__(self):
        super().__init__(
            self.__class__.__name__, self.LOCATOR_MAIN_PAGE_UNIQUE_ELEMENT
        )

    def click_on_the_alert_frame_and_windows_page_button(self):
        button = Button(
            "alert frame and windows button",
            self.LOCATOR_ALERTS_FRAME_AND_WINDOWS_BUTTON,
        )
        BaseForm.scroll_page_down_ot_element(button)
        button.click()

    def click_on_the_elements_page_button(self):
        button = Button(
            "elements button",
            self.LOCATOR_ELEMENTS_BUTTON,
        )
        BaseForm.scroll_page_down_ot_element(button)
        button.click()
