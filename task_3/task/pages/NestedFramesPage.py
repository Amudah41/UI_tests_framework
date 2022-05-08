from task_3.framework.pages.BaseForm import BaseForm
from selenium.webdriver.common.by import By
from task_3.task.elements.Button import Button
from task_3.task.elements.TextField import TextField


class NestedFramesPage(BaseForm):

    LOCATOR_NESTED_FRAMES_PAGE_UNIQUE_ELEMENT = (
        By.XPATH,
        "//div[@id='app']//div[@id='framesWrapper']",
    )

    LOCATOR_LEFT_FORM_NESTED_FRAMES_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"element-list") and contains(@class,"show")]//li[@id="item-3"]',
    )

    LOCATOR_IFRAME_FIELD = (By.XPATH, "//body")

    LOCATOR_LEFT_FORM_FRAMES_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"element-list") and contains(@class,"show")]//li[@id="item-2"]',
    )

    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            self.LOCATOR_NESTED_FRAMES_PAGE_UNIQUE_ELEMENT,
        )

    def click_on_the_left_form_nested_frames_button(self):
        button = Button(
            "left form nested frames button",
            self.LOCATOR_LEFT_FORM_NESTED_FRAMES_BUTTON,
        )

        self.scroll_page_down_ot_element(button)
        button.click()

    def take_iframe_text(self, num):
        return TextField(
            f"iframe {num} text", self.LOCATOR_IFRAME_FIELD
        ).text()

    def click_on_the_left_form_frames_button(self):
        button = Button(
            "left form frames button", self.LOCATOR_LEFT_FORM_FRAMES_BUTTON
        )
        self.scroll_page_down_ot_element(button)
        button.click()
