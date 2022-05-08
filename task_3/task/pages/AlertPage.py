from task_3.framework.pages.BaseForm import BaseForm
from selenium.webdriver.common.by import By
from task_3.task.elements.Button import Button
from task_3.task.elements.TextField import TextField


class AlertPage(BaseForm):

    LOCATOR_ALERT_PAGE_UNIQUE_ELEMENT = (
        By.XPATH,
        "//div[@id='app']//div[@id='javascriptAlertsWrapper']",
    )

    LOCATOR_LEFT_FORM_ALERT_BUTTON = (
        By.XPATH,
        '//div[contains(@class,"element-list") and contains(@class,"show")]//li[@id="item-1"]',
    )

    LOCATOR_ALERT_BUTTON = (By.XPATH, '//button[@id="alertButton"]')

    LOCATOR_ALERT_CONFIRM_BUTTON = (By.XPATH, '//button[@id="confirmButton"]')

    LOCATOR_ALERT_CONFIRM_FIELD = (By.XPATH, '//span[@id="confirmResult"]')

    LOCATOR_ALERT_PROMT_BUTTON = (By.XPATH, '//button[@id="promtButton"]')

    LOCATOR_ALERT_PROMT_FIELD = (By.XPATH, '//span[@id="promptResult"]')

    def __init__(self):
        super().__init__(
            self.__class__.__name__, self.LOCATOR_ALERT_PAGE_UNIQUE_ELEMENT
        )

    def click_on_the_left_form_alert_button(self):
        button = Button(
            "left form alert button", self.LOCATOR_LEFT_FORM_ALERT_BUTTON
        )
        BaseForm.scroll_page_down_ot_element(button)
        button.click()
        BaseForm.scroll_page_up()

    def click_on_the_alert_button(self):
        Button("alert button", self.LOCATOR_ALERT_BUTTON).click()

    def click_on_the_alert_confirm_button(self):
        Button(
            "alert confirm button", self.LOCATOR_ALERT_CONFIRM_BUTTON
        ).click()

    def take_text_after_confirm_alert(self):
        return TextField(
            "text after alert", self.LOCATOR_ALERT_CONFIRM_FIELD
        ).text()

    def click_on_the_alert_promt_button(self):
        Button("alert promt button", self.LOCATOR_ALERT_PROMT_BUTTON).click()

    def take_text_after_promt_alert(self):
        return TextField(
            "text after alert", self.LOCATOR_ALERT_PROMT_FIELD
        ).text()
