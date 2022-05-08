from task_3.framework.pages.BaseForm import BaseForm
from selenium.webdriver.common.by import By
from task_3.task.elements.Button import Button


class BrowserWindowPageLocators:
    LOCATOR_BROWSER_WINDOWS_PAGE_UNIQUE_ELEMENT = (
        By.XPATH,
        "//div[@id='app']//div[@id='browserWindows']",
    )

    LOCATOR_LEFT_FORM_BROWSER_WINDOWS_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"element-list") and contains(@class,"show")]//li[@id="item-0"]',
    )

    LOCATOR_NEW_TAB_BUTTON = (
        By.XPATH,
        '//button[@id="tabButton"]',
    )


class BrowserWindowPage(BaseForm):
    def __init__(self):
        super().__init__(
            self.__class__.__name__,
            BrowserWindowPageLocators.LOCATOR_BROWSER_WINDOWS_PAGE_UNIQUE_ELEMENT,
        )
        self.browser_windows_button = Button(
            "left form browser windows button",
            BrowserWindowPageLocators.LOCATOR_LEFT_FORM_BROWSER_WINDOWS_BUTTON,
        )
        self.new_tab_button = Button(
            "new tab button", BrowserWindowPageLocators.LOCATOR_NEW_TAB_BUTTON
        )

    def click_on_the_left_form_browser_windows_button(self):

        self.browser_windows_button.click()
        BaseForm.scroll_page_up()

    def click_on_the_new_tab_button(self):
        self.new_tab_button.click()
